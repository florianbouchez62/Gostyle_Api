from django.db import models

class Promotion(models.Model):
    libelle = models.CharField("Libelle", max_length=255, unique=True)
    start_date = models.DateTimeField('Date début', null=True)
    end_date = models.DateTimeField('Date fin', null=True)
    pourcentage = models.FloatField("Pourcentage", default=0.0)
    description = models.TextField("Description", max_length=1200)
    image = models.ImageField('Image', blank=True, null=True)
    active = models.BooleanField('Active?', default=False)

    def get_promotion_libelle(self):
        return self.libelle
    
    def get_pourcentage(self):
        return self.pourcentage

    def get_active(self):
        return self.active

    def __repr__(self):
        return self.libelle + "added."