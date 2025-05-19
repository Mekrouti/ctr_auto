import requests
from bs4 import BeautifulSoup
import json
import time

base_urls = [
    "https://mgmindustries.ma/produits_cat/materiel-de-station-pneumatique/",
    "https://mgmindustries.ma/produits_cat/compresseur-a-air/",
    "https://mgmindustries.ma/produits_cat/materiel-de-graissage-et-de-vidange/",
    "https://mgmindustries.ma/produits_cat/redresseur-de-jantes/",
    "https://mgmindustries.ma/produits_cat/materiel-de-charge/",
    "https://mgmindustries.ma/produits_cat/materiel-de-lavage/",
    "https://mgmindustries.ma/produits_cat/materiel-de-diagnostic/",
    "https://mgmindustries.ma/produits_cat/cric-verin-presse-hydraulique/",
    "https://mgmindustries.ma/outillage-industriel/"
]

headers = {"User-Agent": "Mozilla/5.0"}
produits = []

for base_url in base_urls:
    page = 1
    while True:
        url = base_url if page == 1 else f"{base_url}page/{page}/"
        print(f"🔍 Traitement de {url}")

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            print("⏱️ Timeout : Le serveur a mis trop de temps à répondre.")
            break
        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur réseau : {e}")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.select("div.project-item")

        if not items:
            print("✅ Fin de la pagination.")
            break

        for item in items:
            titre_tag = item.select_one("h4.project-title a")
            image_tag = item.select_one("div.xrton-image img")
            lien_tag = item.select_one("div.xrton-image a")
            categorie_tags = item.select("div.project-info p a")

            titre = titre_tag.text.strip() if titre_tag else ""
            image = image_tag["src"] if image_tag else ""
            lien = lien_tag["href"] if lien_tag else ""
            categories = [cat.text.strip() for cat in categorie_tags]

            produits.append({
                "titre": titre,
                "image": image,
                "lien": lien,
                "categories": categories
            })

        page += 1
        time.sleep(2)  # Respect du site

# Sauvegarde dans un fichier JSON
with open("catalogue_mgm_complet.json", "w", encoding="utf-8") as f:
    json.dump(produits, f, ensure_ascii=False, indent=4)

print(f"✅ {len(produits)} produits extraits et sauvegardés.")
