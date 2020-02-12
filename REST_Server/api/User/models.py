from django.db import models

class Promotion(models.Model):
    libelle = models.CharField("Libelle", max_length=255, unique=True)
    start_date = models.DateTimeField('Date début', auto_now=True)
    end_date = models.DateTimeField('Date fin', blank=True, null=True)
    pourcentage = models.FloatField("Pourcentage", default=1.0)
    description = models.TextField("Description", max_length=1200)

    def get_promotion_libelle(self):
        return self.libelle

    def __repr__(self):
        return self.libelle + "added."