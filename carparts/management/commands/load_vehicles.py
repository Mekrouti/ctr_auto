from django.core.management.base import BaseCommand
from carparts.models import Vehicle
import json

class Command(BaseCommand):
    help = 'Charge les véhicules depuis un fichier JSON'

    def handle(self, *args, **kwargs):
        try:
            with open("carparts/vehicles.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            for item in data:
                fields = item["fields"]
                Vehicle.objects.create(
                    marque_id=fields.get("marque_id", 0),
                    marque=fields.get("marque", ""),
                    model_id=fields.get("model_id", 0),
                    model_name=fields.get("model_name", ""),
                    vehicle_id=fields.get("vehicle_id", 0),
                    vehicle_name=fields.get("vehicle_name", ""),
                    engine=fields.get("engine", ""),
                    year=fields.get("year", ""),
                    logo=fields.get("logo", None),
                    self_url=fields.get("self_url", ""),
                )

            self.stdout.write(self.style.SUCCESS("Véhicules importés avec succès."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erreur : {e}"))
