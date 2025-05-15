from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import time

# Configuration du navigateur
options = webdriver.ChromeOptions()
options.add_argument("--headless")
service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Première page
url = "https://mgmindustries.ma/produits_cat/materiel-de-carrosserie/"
driver.get(url)
time.sleep(2)

produits = []

while True:
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    items = soup.select("div.project-item")
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

    # Vérifie la présence d’un bouton "Next" (page suivante)
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'a.next.page-numbers')
        next_button.click()
        time.sleep(2)
    except:
        print("✅ Fin de la pagination.")
        break

driver.quit()

# Sauvegarde en JSON
with open("catalogue_materiel_carrosserie.json", "w", encoding="utf-8") as f:
    json.dump(produits, f, ensure_ascii=False, indent=4)

print(f"✅ {len(produits)} produits extraits.")
