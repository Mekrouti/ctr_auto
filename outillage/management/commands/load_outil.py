import json
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from outillage.models import Category, Product


class Command(BaseCommand):
    help = "Charge les catégories puis les produits (Category.json, Product.json)"

    def handle(self, *args, **options):
        base_dir = Path.cwd()          # place les deux fichiers au même endroit
        cat_file = base_dir / "category_outil.json"
        prod_file = base_dir / "catalogue_mgm_complet.json"

        # --- 1.  Catégories --------------------------------------------------
        try:
            categories = json.loads(cat_file.read_text(encoding="utf‑8"))
        except FileNotFoundError:
            raise CommandError("category_outil.json introuvable")

        for item in categories:
            fields = item["fields"]
            cat, created = Category.objects.get_or_create(
                name=fields["name"].strip(),
                defaults={
                    "url":   fields.get("url", ""),
                    "image": fields.get("image", "")
                },
            )
            action = "🆕 ajoutée" if created else "✓ existait"
            self.stdout.write(f"{action} : {cat.name}")

        # --- 2.  Produits -----------------------------------------------------
        try:
            products = json.loads(prod_file.read_text(encoding="utf‑8"))
        except FileNotFoundError:
            raise CommandError("Product.json introuvable")

        for item in products:
            fields = item["fields"]
            titre = fields["titre"].strip()
            lien = fields.get("lien")
            if not lien:
                 self.stderr.write(f"⚠️  Lien manquant, produit ignoré : {titre}")
                 continue
            lien = lien.strip()
            cat_name = fields["category"].strip()

            try:
                cat = Category.objects.get(name=cat_name)
            except Category.DoesNotExist:
                self.stderr.write(f"❌ Catégorie inconnue : {cat_name} (produit « {titre} »)")
                continue

            prod, created = Product.objects.get_or_create(
                lien=lien,
                defaults={
                    "titre":    titre,
                    "image":    fields.get("image", ""),
                    "category": cat,
                },
            )
            if not created:
                prod.titre    = titre
                prod.image    = fields.get("image", "")
                prod.category = cat
                prod.save()
            action = "🆕 ajouté" if created else "✓ mis à jour"
            self.stdout.write(f"{action} : {titre}")
