from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    image = models.URLField()

    def __str__(self):
        return self.name