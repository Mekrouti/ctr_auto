import os
import json
from django.core.management.base import BaseCommand
from accessoire.models import Accessoire

class Command(BaseCommand):
    help = 'Charge des accessoires depuis un fichier JSON'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(os.path.dirname(__file__), 'jumia_catalog.json')

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"Fichier non trouvé : {file_path}"))
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            fields = item.get('fields', {})

            name = fields.get('name', '').strip()
            description = fields.get('description', '')
            lien = fields.get('Lien', '')
            image = fields.get('image', '')
            price_str = fields.get('price', '0')

            if isinstance(price_str, str) and "Dhs" in price_str:
                price_str = price_str.replace("Dhs", "").strip()

            try:
                price = float(price_str)
            except ValueError:
                self.stdout.write(self.style.WARNING(f"Prix invalide pour {name}, ignoré."))
                continue

            obj, created = Accessoire.objects.get_or_create(
                name=name,
                defaults={
                    'description': description,
                    'price': price,
                    'Lien': lien,
                    'image': image,
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Ajouté : {obj.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Déjà existant : {obj.name}"))
