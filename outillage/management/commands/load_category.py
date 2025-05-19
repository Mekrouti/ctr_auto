import json
from django.core.management.base import BaseCommand
from outillage.models import Category

class Command(BaseCommand):
    help = "Charger les catégories depuis un fichier JSON"

    def handle(self, *args, **options):
        with open("category_outil.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            try:
                fields = item["fields"]
                name = fields["name"]
                url = fields.get("url", "")
                image = fields.get("image", "")

                cat, created = Category.objects.get_or_create(
                    name=name,
                    defaults={"url": url, "image": image}
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"🆕 Catégorie ajoutée : {name}"))
                else:
                    self.stdout.write(f"✅ Catégorie déjà existante : {name}")

            except Exception as e:
                self.stderr.write(f"❌ Erreur avec l'entrée : {item}\n{e}")
