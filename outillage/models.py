from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    image = models.URLField()

    def __str__(self):
        return self.name


class Product(models.Model):  # anciennement "SubCategory"
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # ✅ Champ ajouté

    image = models.URLField()
    titre = models.CharField(max_length=255)
    lien = models.URLField(unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

