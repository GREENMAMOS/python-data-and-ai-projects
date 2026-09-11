"""Portfolio refactor of the user's dynamic-page collection exercise."""
import re
import time
from urllib.parse import urljoin
from bs4 import BeautifulSoup

URL = "https://store.kakao.com/home/talkdeal/category/0"
FIELDS = ["상품명", "상세페이지링크", "가격", "판매처", "배송정보"]


def parse_price(text):
    value = text.split("원")[0].replace(",", "").strip()
    if not re.fullmatch(r"\d+", value):
        raise ValueError(f"Unsupported price format: {text!r}")
    return int(value)


def parse_products(html):
    rows = []
    for item in BeautifulSoup(html, "html.parser").select(".item_product"):
        name = item.select_one(".name_product")
        link = item.select_one(".link_product")
        price = item.select_one(".txt_price")
        store = item.select_one(".tit_store")
        delivery = item.select_one(".group_others > .ng-star-inserted")
        if not all([name, link, price, store]) or not link.get("href"):
            raise ValueError("Required product fields missing; inspect page structure")
        rows.append(dict(zip(FIELDS, [name.get_text(strip=True), urljoin(URL, link["href"]),
                    parse_price(price.get_text(strip=True)), store.get_text(strip=True),
                    delivery.get_text(" ", strip=True) if delivery else None])))
    return rows


def collect(max_scrolls=5):
    """Network/browser access only when explicitly called; live site unverified."""
    from selenium import webdriver
    driver = webdriver.Chrome()
    try:
        driver.get(URL)
        height = driver.execute_script("return document.body.scrollHeight")
        for _ in range(max_scrolls):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == height:
                break
            height = new_height
        return parse_products(driver.page_source)
    finally:
        driver.quit()
