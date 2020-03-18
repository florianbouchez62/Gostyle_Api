from django.db import models

class PromotionManager(models.Manager):
    
    def create_promotion(self, libelle, description, start_date=None, end_date=None, pourcentage=0.0, image=None, active=False):
        promotion = Promotion.objects.create(
            libelle=libelle, 
            start_date=start_date,
            end_date=end_date,
            pourcentage=pourcentage,
            description=description,
            image=image,
            active=active
        )
        return promotion


class Promotion(models.Model):
    libelle = models.CharField("Libelle", max_length=255, unique=True)
    description = models.TextField("Description", max_length=1200)
    start_date = models.DateTimeField('Date début', null=True)
    end_date = models.DateTimeField('Date fin', null=True)
    pourcentage = models.FloatField("Pourcentage", default=0.0)
    image = models.ImageField('Image', blank=True, null=True)
    active = models.BooleanField('Active?', default=False)

    objects = PromotionManager()

    def get_promotion_libelle(self):
        return self.libelle
    
    def get_pourcentage(self):
        return self.pourcentage

    def get_active(self):
        return self.active

    def __repr__(self):
        return self.libelle + " added."
