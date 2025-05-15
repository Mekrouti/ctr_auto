from django.core.management.base import BaseCommand
from carparts.models import Category_auto_parts, SubCategory_auto_parts
import json

class Command(BaseCommand):
    help = 'Charge les données des pièces auto'

    def handle(self, *args, **kwargs):
        try:
            with open("carparts/categories_autoparts.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            for item in data:
                fields = item["fields"]
                category = Category_auto_parts.objects.create(
                    name=fields["name"],
                    img=fields["img"],
                    self_url=fields["self"],
                    leaf=fields["leaf"],
                    recommendedQuantity=fields["recommendedQuantity"],
                )

                for sub in fields.get("subcategories", []):
                    sub_fields = sub["fields"]
                    SubCategory_auto_parts.objects.create(
                        category=category,
                        name=sub_fields["name"],
                        img=sub_fields["img"],
                        self_url=sub_fields["self"],
                        leaf=sub_fields["leaf"],
                        recommendedQuantity=sub_fields["recommendedQuantity"],
                    )

            self.stdout.write(self.style.SUCCESS("Importation réussie."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erreur : {e}"))