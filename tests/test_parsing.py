import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from offline_demo import load


class ParsingTests(unittest.TestCase):
    def test_riss_field_order_and_missing(self):
        parser = load("riss")
        html = (ROOT / "projects/riss/fixtures/detail.html").read_text(encoding="utf-8")
        self.assertEqual(parser.parse_detail(html), {"publisher": "예시 기관", "year": "2025", "keywords": ["데이터", "분석"]})
        self.assertEqual(parser.parse_detail("<ul></ul>"), {"publisher": None, "year": None, "keywords": []})

    def test_riss_links_and_pagination(self):
        parser = load("riss")
        rows = parser.parse_results((ROOT / "projects/riss/fixtures/search.html").read_text(encoding="utf-8"))
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["url"], "https://www.riss.kr/example/1")
        self.assertEqual(parser.build_params("example", 2, 10)["iStartCount"], 10)

    def test_product_normalization(self):
        parser = load("shopping")
        rows = parser.parse_products((ROOT / "projects/shopping/fixtures/products.html").read_text(encoding="utf-8"))
        self.assertEqual([r["가격"] for r in rows], [12900, 8000])
        self.assertEqual(rows[0]["배송정보"], "무료배송")
        self.assertIsNone(rows[1]["배송정보"])
        with self.assertRaises(ValueError):
            parser.parse_price("가격 문의")
        with self.assertRaises(ValueError):
            parser.parse_products('<div class="item_product"></div>')


if __name__ == "__main__":
    unittest.main()
