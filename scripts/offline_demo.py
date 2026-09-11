"""Run from repository root. Reads synthetic fixtures; does not access a network."""
import csv
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "projects" / name / "collector.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    out = ROOT / "outputs"
    out.mkdir(exist_ok=True)
    riss, shopping = load("riss"), load("shopping")
    base = ROOT / "projects" / "riss" / "fixtures"
    papers = riss.parse_results((base / "search.html").read_text(encoding="utf-8"))
    for i, row in enumerate(papers):
        row.update(riss.parse_detail((base / "detail.html").read_text(encoding="utf-8") if i == 0 else "<ul></ul>"))
    (out / "papers-synthetic.json").write_text(json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8")
    products = shopping.parse_products((ROOT / "projects/shopping/fixtures/products.html").read_text(encoding="utf-8"))
    with (out / "products-synthetic.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=shopping.FIELDS)
        writer.writeheader()
        writer.writerows(products)
    print(f"Synthetic fixtures only: {len(papers)} papers, {len(products)} products -> outputs/")


if __name__ == "__main__":
    main()
