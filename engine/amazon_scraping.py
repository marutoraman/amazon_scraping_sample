from math import asin
from bs4 import BeautifulSoup as bs
import re

from selenium.webdriver import Chrome
from common.driver import set_driver

AMAZON_DOMAIN = "https://www.amazon.co.jp/"

class AmazonItem():

    def __init__(self, name:str=None, description:str=None, price:int=None, 
                 asin:str=None, star:float=None):
        self.name = name
        self.description = description
        self.price = price
        self.asin = asin
        self.star = star

class AmazonScraping():

    def __init__(self):
        self.driver = set_driver()


    def fetch_item(self, url: str) -> AmazonItem:
        self.driver.get(url)
        
        # 商品名
        try:
            name = self.driver.find_element_by_css_selector("#productTitle").text.strip()
        except:
            name = None
            
        # 説明
        try:
            description = self.driver.find_element_by_css_selector("#productDescription").text.strip().replace("\n","")
        except:
            description = None

        # 価格
        try:
            price = int(self.driver.find_element_by_css_selector("#priceblock_ourprice").text.replace("￥","").replace(",",""))
        except:
            price = None
        
        # 星の数
        try:
            star = float(self.driver.find_element_by_css_selector(".a-icon-alt").text.replace("5つ星のうち",""))
        except:
            star = None
        
        # ASIN (urlの/dp/の後の英数字10桁)
        m = re.search(r"/dp/(\w{10})", url)
        try:
            asin = m.group(1)
        except:
            asin = None
        
        return AmazonItem(
            name=name, description=description, price=price,
            asin=asin, star=star
        )

    
    def fetch_ranking_items(self, url: str, limit:int=50) -> list:
        # Driver起動
        try:
            driver = set_driver()
        except:
            print("selenium driver起動エラー")
            raise Exception("selenium driver起動エラー")
        
        # ランキングページを開く
        driver.get(url)
        
        # ランキングitemの要素を取得
        item_elms = driver.find_elements_by_css_selector(".aok-inline-block.zg-item > a")
                
        # 商品詳細のリンクを取得
        item_links = []
        for i, item_elm in enumerate(item_elms[:limit]):
            try:
                # linkを取得
                item_links.append(item_elm.get_attribute("href"))
            except Exception as e:
                pass
        print(f"item count: {len(item_links)}")
        
        items = []    
        for i, item_link in enumerate(item_links):
            try:
                # itemの情報を取得
                item = self.fetch_item(item_link)
                items.append(item)
                print(f"{i+1} 個目取得完了")
            except Exception as e:
                print(f"error {item_link} | {e}")
        print(len(items))

        return items
