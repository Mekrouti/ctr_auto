from django.db import models

# Create your models here.




# Modèle pour les catégories
class Category(models.Model):
    Car_category = [
        ('coupe', 'Coupé'),       # Voiture à deux portes, généralement sportive
        ('sedan', 'Berline'),    # Voiture à quatre portes
        ('suv', 'SUV'),          # Véhicule utilitaire sport
        ('hatchback', 'Hayon'),  # Voiture avec un coffre intégré
        ('convertible', 'Cabriolet'),  # Voiture décapotable
        ('van', 'Van'),          # Véhicule utilitaire ou familial
        ('pickup', 'Pick-up'),   # Véhicule avec un espace de chargement
        ('wagon', 'Break'),      # Voiture avec un grand espace de chargement
        ('truck', 'Camion'),     # Véhicule de transport lourd
    ]

    name = models.CharField(max_length=50, choices=Car_category, unique=True)
    def __str__(self):
        # Retourne une version lisible de la catégorie
        return self.get_name_display()
# Modèle pour les marques de voitures
class Marques(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom de la marque")

    def __str__(self):
        return self.name




# Modèle pour les voitures
class Cars(models.Model):
    marque = models.ForeignKey(Marques, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    image_left = models.ImageField(upload_to='cars/', blank=True, null=True)
    image_right = models.ImageField(upload_to='cars/', blank=True, null=True)
    image_front = models.ImageField(upload_to='cars/', blank=True, null=True)
    image_back = models.ImageField(upload_to='cars/', blank=True, null=True)
    image_side = models.ImageField(upload_to='cars/', blank=True, null=True)
    habitacl = models.ImageField(upload_to='cars/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    km = models.PositiveIntegerField(help_text='Kilométrage en kilomètres')
    Puissance_fiscale = models.DecimalField(max_digits=5, decimal_places=2)
    Origine = models.CharField(max_length=30, choices=[
        ('Dédouanée', 'Dedouanèe'),
        ('pas encore Dédouanée ','pas encore Dédouanée '),
        ( 'WW au Maroc' ,'WW au Maroc')])
    Première_main = models.CharField(max_length=30, choices=[
        ('Oui', 'Oui'),
        ('Non', 'Non')])

    status = models.CharField(max_length=20, choices=[
        ('available', 'Disponible'),
        ('sold', 'Vendu')

        ])
    Boite_de_vitesses= models.CharField(max_length=20,
    choices=[
        ('Automatique', 'Automatique'),
        ('Manuelle', 'Manuelle'),
    ])
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    IMAGE_MAX_SIZE = (800, 800)

    def __str__(self):
        return f"{self.marque} {self.model} ({self.year})"

    def resize_image(self, image_field):
        """Redimensionner l'image si elle existe et est valide."""
        if image_field and hasattr(image_field, 'path'):
            try:
                with Image.open(image_field.path) as image:
                    image.thumbnail(self.IMAGE_MAX_SIZE)
                    image.save(image_field.path)
            except Exception as e:
                print(f"Erreur lors du redimensionnement de l'image {image_field.name}: {e}")

    def save(self, *args, **kwargs):
        """Sauvegarde le modèle et redimensionne les images."""
        super().save(*args, **kwargs)
        self.resize_image(self.image_front)
        self.resize_image(self.image_back)
        self.resize_image(self.image_side)
        self.resize_image(self.image_left)
        self.resize_image(self.image_right)
