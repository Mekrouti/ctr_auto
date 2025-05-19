import requests
from bs4 import BeautifulSoup
import json

url = "https://mgmindustries.ma/details/cabine-de-peinture-astra/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # ✅ Titre (h2.page-title dans le haut de la page)
    title_tag = soup.find("h2", class_="page-title")
    title = title_tag.text.strip() if title_tag else "Titre non trouvé"

    # ✅ Description (tout le texte dans la partie info)
    desc_container = soup.find("div", class_="portfolio-info")
    description = desc_container.get_text(separator="\n", strip=True) if desc_container else "Description non trouvée"

    # ✅ Images dans div class="portfolio-images"
    image_tags = soup.select("div.portfolio-images img")
    image_urls = [img["src"] for img in image_tags if img.get("src")]

    # ✅ Assemblage des données
    data = {
        "title": title,
        "description": description,
        "images": image_urls
    }

    # ✅ Sauvegarde du JSON
    with open("cabine_peinture.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("✅ Données sauvegardées dans cabine_peinture.json")

else:
    print(f"❌ Erreur lors de la récupération de la page : {response.status_code}")
