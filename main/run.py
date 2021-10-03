import os
import sys
import pandas as pd
import fire

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from engine.amazon_scraping import *


def run(url: str, limit:int=50):
    amazon = AmazonScraping()
    items = amazon.fetch_ranking_items(url, limit)
    df = pd.DataFrame()
    for item in items:
        df = df.append(item.__dict__, ignore_index=True).fillna("")
    df.to_csv("./export_items.csv", encoding="utf-8_sig", columns=["name", "asin", "price", "star", "description"])


if __name__ == "__main__":
    fire.Fire(run)
    #run("https://www.amazon.co.jp/gp/bestsellers/automotive", 3)