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
        pass

    
    @staticmethod
    def fetch_ranking_items(url: str, limit:int=50) -> list:
        pass
