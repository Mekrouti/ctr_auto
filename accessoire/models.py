
from django.db import models
from carparts.models import Vehicle  # si tu veux lier les accessoires aux véhicules


class Accessoire(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # Utilise URLField au lieu de ImageField si l'image vient d’un lien externe
    image = models.URLField(blank=True, null=True)

    # Ce champ est utilisé dans ton JSON pour stocker le lien Jumia
    Lien = models.URLField(blank=True, null=True)

    compatible_vehicles = models.ManyToManyField(Vehicle, related_name='accessoires', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
