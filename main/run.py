import os
import sys
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from engine.amazon_scraping import *


def run(url: str, limit:int=50):
    pass


if __name__ == "__main__":
    run("https://www.amazon.co.jp/gp/bestsellers/automotive", 3)