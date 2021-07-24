from math import asin
from bs4 import BeautifulSoup as bs
import re

from selenium.webdriver import Chrome
from common.driver import set_driver

AMAZON_DOMAIN = "https://www.amazon.co.jp/"

class AmazonItem():

    def __init__(self, name:str, description:str, price:int, 
                 asin:str, star:float):
        self.name = name
        self.description = description
        self.price = price
        self.asin = asin
        self.star = star


class AmazonScraping():

    @staticmethod
    def fetch_item(driver:Chrome, url: str) -> AmazonItem:
        driver.get(url)
        soup = bs(driver.page_source, "html.parser")
        
        # 商品名
        name = soup.select_one("#productTitle").text.strip() if soup.select_one("#productTitle") != None else None

        # 説明
        description = soup.select_one("#productDescription").text.strip().replace("\n","") if soup.select_one("#productDescription") != None else None

        # 価格
        price = int(soup.select_one("#priceblock_ourprice").text.replace("￥","").replace(",","")) if soup.select_one("#priceblock_ourprice") != None else None
        
        # 星の数
        star = None
        if soup.select_one(".a-icon-alt") != None and soup.select_one(".a-icon-alt").text.find("5つ星のうち") >= 0:
            star = float(soup.select_one(".a-icon-alt").text.replace("5つ星のうち",""))

        # ASIN (urlの/dp/の後の英数字10桁)
        m = re.search(r"/dp/(\w{10})", url)
        asin = m.group(1) if m != None else None

        return AmazonItem(
            name=name, description=description, price=price,
            asin=asin, star=star
        )

    
    @staticmethod
    def fetch_ranking_items(url: str, limit:int=50) -> list:
        # Driver起動
        try:
            driver = set_driver()
        except:
            print("selenium driver起動エラー")
            raise Exception("selenium driver起動エラー")
        # ランキングページを開く
        driver.get(url)
        soup = bs(driver.page_source, "html.parser")
        # ランキングitemの要素を取得
        item_elms = soup.select(".aok-inline-block.zg-item > a")
        items = []
        for i, item_elm in enumerate(item_elms[:limit]):
            # linkを取得
            item_link = item_elm.get("href")
            # itemの情報を取得
            items.append(AmazonScraping.fetch_item(driver, AMAZON_DOMAIN + item_link))
            print(f"{i+1} 個目取得完了")
        print(len(items))

        return items
