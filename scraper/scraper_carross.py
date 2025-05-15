from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
import json
from bs4 import BeautifulSoup
import time

# Configuration du driver
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://monpartenairecarrossier.fr/pieces/"
driver.get(url)

# Cliquer sur "Charger plus de produits" tant qu'il est visible
while True:
    try:
        charger_plus = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "loadMore-button"))
        )
        driver.execute_script("arguments[0].click();", charger_plus)
        print("Chargement de plus de produits...")
        time.sleep(2)
    except:
        print("Tous les produits ont été chargés.")
        break

# Récupération du HTML après chargement complet
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Création du dossier pour les images
os.makedirs("images", exist_ok=True)

# Liste pour stocker les produits
produits_data = []

# Sélection des produits
produits = soup.select("ul#loadMore-list li")

for i, produit in enumerate(produits, start=1):
    try:
        titre = produit.select_one("h3.product-title").get_text(strip=True)
        prix = produit.select_one("p.product-price span:not(.stroke)").get_text(strip=True)
        lien = produit.select_one("a")["href"]
        image_url = produit.select_one("img")["src"]

        print(f"{i}. {titre} | {prix} | {lien}")

        # Téléchargement de l'image
        image_data = requests.get(image_url).content
        image_name = f"{titre.replace(' ', '_').replace('/', '_')[:50]}.jpg"
        with open(f"images/{image_name}", 'wb') as f:
            f.write(image_data)

        # Ajout aux données JSON
        produits_data.append({
            "titre": titre,
            "prix": prix,
            "lien": lien,
            "image": image_name
        })

    except Exception as e:
        print(f"Erreur pour un produit : {e}")

driver.quit()

# Enregistrement dans un fichier JSON
with open("produits.json", "w", encoding="utf-8") as f:
    json.dump(produits_data, f, ensure_ascii=False, indent=4)

print("Données enregistrées dans produits.json.")
