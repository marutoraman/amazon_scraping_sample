from amazon_scraping import *

def test_amazon_scraping():
    driver = set_driver()
    res = AmazonScraping.fetch_item(driver, "https://www.amazon.co.jp/Canon-%E3%82%A4%E3%83%B3%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%88%E3%82%AB%E3%83%A1%E3%83%A9%E3%83%97%E3%83%AA%E3%83%B3%E3%82%BF%E3%83%BC-iNSPiC-CV-123-WH-%E3%83%9B%E3%83%AF%E3%82%A4%E3%83%88/dp/B07S49FFWJ?ref_=Oct_obs_d_8443112051&pd_rd_w=6CdSZ&pf_rd_p=2a1107bd-12d7-491a-b20d-ebdadf92e435&pf_rd_r=R2YC605WESGRD70ZAX3Q&pd_rd_r=96499f9d-a3b3-4515-a238-e6b3d44f10f5&pd_rd_wg=Bamdr&pd_rd_i=B07S49FFWJ")
    print(res.__dict__)
    assert res.name
    assert res.price 


def test_fetch_ranking_items():
    res = AmazonScraping.fetch_ranking_items("https://www.amazon.co.jp/gp/bestsellers/automotive")
    assert len(res) >= 1