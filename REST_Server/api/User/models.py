from django.db import models

class Promotion(models.Model):
    libelle = modesl.CharField("Libelle", max_length=255)
    start_date = models.DateTimeField('Date début', auto_now=True)
    end_date = models.DateTimeField('Date fin', blank=True, null=True)
    pourcentage = models.FloatField("Pourcentage", default=0.0)
