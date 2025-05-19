import json, os, time, requests
from pathlib import Path

BASE    = "https://cartec.ma/"                # domaine pour compléter les URLs d’images

# ──────────────────────────────
# 1. Charger les fichiers locaux
# ──────────────────────────────
with open("carparts/categories_autoparts.json", encoding="utf-8") as f:
    categories = json.load(f)

with open("carparts/vehicles.json", encoding="utf-8") as f:
    vehicles = json.load(f)

# ──────────────────────────────
# 2. Extraire les IDs feuilles
# ──────────────────────────────
def leaf_ids(nodes):
    out = []
    for n in nodes:
        if n.get("leaf"):
            out.append(n["id"])
        out += leaf_ids(n.get("subs", []))
    return out

category_ids = leaf_ids(categories)
vehicle_ids  = [v["fields"]["vehicle_id"] for v in vehicles]

# ──────────────────────────────
# 3. Préparer les dossiers
# ──────────────────────────────
Path("images").mkdir(exist_ok=True)
Path("json_pages").mkdir(exist_ok=True)

results = []

# ──────────────────────────────
# 4. Boucle principale
# ──────────────────────────────
for cat in category_ids:
    for veh in vehicle_ids:
        page = 1
        while True:
            url = API_TPL.format(cat=cat, veh=veh, page=page)
            try:
                resp = requests.get(url, timeout=15)
                resp.raise_for_status()
                payload = resp.json().get("data", {})
                parts   = payload.get("parts", [])

                if not parts:
                    break          # aucune pièce sur cette page → page suivante inutile

                # Optionnel : conserver la page brute pour debug
                with open(f"json_pages/{cat}_{veh}_p{page}.json", "w", encoding="utf-8") as fp:
                    json.dump(parts, fp, ensure_ascii=False, indent=2)

                for p in parts:
                    img_rel = p.get("articleImg") or ""          # /api/images/...
                    img_url = BASE + img_rel                     # URL absolue
                    img_name = img_rel.split("/")[-1]            # 199a65....jpg

                    # Télécharger l’image si elle n’existe pas déjà
                    img_path = Path("images") / img_name
                    if img_rel and not img_path.exists():
                        try:
                            img_data = requests.get(img_url, timeout=15).content
                            img_path.write_bytes(img_data)
                        except Exception as e:
                            print(f"   Image KO {img_url} → {e}")

                    # Ajouter la ligne de résultat
                    results.append({
                        "category_id" : cat,
                        "vehicle_id"  : veh,
                        "article_id"  : p["id"],
                        "article_name": p["articleName"],
                        "brand"       : p.get("brand", {}).get("name"),
                        "price"       : p.get("discountPrice"),
                        "inStock"     : p.get("inStock"),
                        "image_file"  : str(img_path),
                        "image_url"   : img_url
                    })

                page += 1
                time.sleep(0.25)        # courte pause anti‑ban
            except Exception as err:
                print(f"[!] {url} → {err}")
                break

# ──────────────────────────────
# 5. Sauvegarde finale
# ──────────────────────────────
with open("cartec_parts.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"✅ Scraping terminé : {len(results)} pièces collectées")
