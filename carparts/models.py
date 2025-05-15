from django.db import models

# Create your models here.




class Vehicle(models.Model):
    marque_id = models.IntegerField()
    marque = models.CharField(max_length=100)
    model_id = models.IntegerField()
    model_name = models.CharField(max_length=150)
    vehicle_id = models.IntegerField()
    vehicle_name = models.CharField(max_length=200)
    engine = models.CharField(max_length=150)
    year = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)  # à condition de gérer les médias
    self_url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.marque} {self.model_name} - {self.engine}"
    







class Category_auto_parts(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/cats/')
    self_url = models.CharField(max_length=255)  # évite d’utiliser `self` comme nom de champ
    leaf = models.BooleanField(default=False)
    recommendedQuantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class SubCategory_auto_parts(models.Model):
    category = models.ForeignKey(Category_auto_parts, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/cats/')
    self_url = models.CharField(max_length=255)  # idem
    leaf = models.BooleanField(default=False)
    recommendedQuantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name