import requests
from bs4 import BeautifulSoup
import json

url = "https://mgmindustries.ma"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

categories = []

for col in soup.select(".wpb_column.vc_col-sm-1\\/5"):
    img_tag = col.find("img")
    link_tag = col.find("a", href=True)
    title_tag = col.find("h5")

    if img_tag and link_tag and title_tag:
        categories.append({
            "name": title_tag.get_text(strip=True),
            "url": link_tag["href"],
            "image": img_tag["src"]
        })

with open("category_outil.json", "w", encoding="utf-8") as f:
    json.dump(categories, f, indent=2, ensure_ascii=False)
print("✅ Catalogue enregistré dans 'category_outil.json'")
