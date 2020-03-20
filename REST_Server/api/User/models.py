from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class Promotion(models.Model):
    libelle = models.CharField("Libelle", max_length=255, unique=True)
    description = models.TextField("Description", max_length=1200)
    start_date = models.DateTimeField('Date début', null=True)
    end_date = models.DateTimeField('Date fin', null=True)
    pourcentage = models.FloatField("Pourcentage", default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    image = models.ImageField('Image', blank=True, null=True)
    active = models.BooleanField('Active?', default=False)

    def clean(self):
        cleaned_data = super().clean()
        if self.start_date <= timezone.now():
            raise ValidationError('The start date must be greater than the current date.')
        if (self.start_date >= self.end_date):
            raise ValidationError('The end date must be greater than the start date.')
        return cleaned_data
#
    def get_promotion_libelle(self):
        return self.libelle
    
    def get_pourcentage(self):
        return self.pourcentage

    def get_active(self):
        return self.active

    def __repr__(self):
        return self.libelle + " added."
