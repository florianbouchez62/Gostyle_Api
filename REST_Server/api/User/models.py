from django.db import models

class Article(models.Model):
    libelle = models.CharField("Libelle", max_length=128)
    prix = models.FloatField("Prix", default=0.0)

    def __str__(self):
        return str(self.libelle)

class Promotion(models.Model):
    article = models.ForeignKey(Article,
                            verbose_name="Article",
                            on_delete=models.CASCADE)
    pourcentage = models.FloatField("Pourcentage", default=0.0)
    qrCode = models.CharField("Qrcode", max_length=20)
