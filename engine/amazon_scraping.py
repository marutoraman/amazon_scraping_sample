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


    def fetch_item(self, url: str):
        pass

    
    def fetch_ranking_items(self, url: str, limit:int=50):
        pass
