from django.db import models

class Promotion(models.Model):
    libelle = models.CharField("Libelle", max_length=255, unique=True)
    start_date = models.DateTimeField('Date début')
    end_date = models.DateTimeField('Date fin')
    pourcentage = models.FloatField("Pourcentage", default=1.0)
    description = models.TextField("Description", max_length=1200)
    image = models.ImageField('Image', blank=True, null=True)
    active = models.BooleanField('Active?', default=False)

    def get_promotion_libelle(self):
        return self.libelle

    def __repr__(self):
        return self.libelle + "added."