from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class Promotion(models.Model):
    name = models.CharField("Name", max_length=255, unique=True)
    description = models.TextField("Description", max_length=1200)
    start_date = models.DateTimeField('Start date', null=True)
    end_date = models.DateTimeField('End date', null=True)
    percentage = models.FloatField("Percentage", default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    image = models.ImageField('Image', blank=True, null=True)
    qrcode = models.ImageField(upload_to='', blank=True, null=True)
    active = models.BooleanField('Active ?', default=False)

    def clean(self):
        cleaned_data = super().clean()
        if self.start_date <= timezone.now():
            raise ValidationError('The start date must be greater than the current date.')
        if (self.start_date >= self.end_date):
            raise ValidationError('The end date must be greater than the start date.')
        return cleaned_data

    def get_promotion_name(self):
        return self.name
    
    def get_percentage(self):
        return self.percentage

    def get_active(self):
        return self.active

    def __repr__(self):
        return self.name + " added."
