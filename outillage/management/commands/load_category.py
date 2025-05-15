from django.core.management.base import BaseCommand
import json
# Configure Django (à adapter à ton projet)

from outillage.models import Category  # ← Ton vrai modèle ici

class Command(BaseCommand):
    help = "Charge les catégories depuis un fichier JSON"

    def handle(self, *args, **kwargs):
        with open("category_outil.json", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            Category.objects.get_or_create(
                name=item["name"],
                url=item["url"],
                image=item["image"]
            )

        self.stdout.write(self.style.SUCCESS("Import terminé."))


