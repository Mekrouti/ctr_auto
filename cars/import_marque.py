import csv
from cars.models import Marques

with open('cars/marques.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        marque_id = int(row['id'])
        name = row['name'].strip()

        # Crée ou met à jour l'objet
        obj, created = Marques.objects.update_or_create(
            id=marque_id,
            defaults={'name': name}
        )
        print(f"{'Créé' if created else 'Mis à jour'}: {obj.name}")

        exec(open('cars/import_marque.py').read())

        


        

