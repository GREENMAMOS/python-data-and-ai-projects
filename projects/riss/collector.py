"""Original learning workflow, reorganized for portfolio review; no calls on import."""
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

SEARCH_URL = "https://www.riss.kr/search/Search.do"


def build_params(query, page=1, page_size=10):
    if page < 1 or not 1 <= page_size <= 100:
        raise ValueError("page >= 1 and 1 <= page_size <= 100 required")
    return dict(isDetailSearch="N", searchGubun="true", viewYn="OP",
                strQuery=query, order="/DESC", onHanja="false", strSort="RANK",
                iStartCount=(page - 1) * page_size, sflag=1, isFDetailSearch="N",
                pageNumber=page, resultKeyword=query, icate="re_a_kor",
                colName="re_a_kor", pageScale=page_size, isTab="Y", query=query)


def parse_results(html):
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for item in soup.select(".srchResultListW > ul > li"):
        anchor = item.select_one(".title > a")
        if anchor and anchor.get("href"):
            rows.append({"title": anchor.get_text(" ", strip=True),
                         "url": urljoin(SEARCH_URL, anchor["href"])})
    return rows


def parse_detail(html):
    soup = BeautifulSoup(html, "html.parser")

    def value(label):
        node = soup.find("span", string=lambda s: s and s.strip() == label)
        sibling = node.find_next_sibling() if node else None
        return sibling.get_text(" ", strip=True) if sibling else None

    keywords = value("주제어")
    return {"publisher": value("발행기관"), "year": value("발행연도"),
            "keywords": [s.strip() for s in keywords.split(";") if s.strip()]
            if keywords else []}


def collect(query, page=1, page_size=10):
    """Explicit opt-in network function. Current live selectors are unverified."""
    with requests.Session() as session:
        response = session.get(SEARCH_URL, params=build_params(query, page, page_size), timeout=20)
        response.raise_for_status()
        rows = parse_results(response.text)
        for row in rows:
            detail = session.get(row["url"], headers={"User-Agent": "Mozilla/5.0",
                                 "Referer": response.url}, timeout=20)
            detail.raise_for_status()
            row.update(parse_detail(detail.text))
        return rows
