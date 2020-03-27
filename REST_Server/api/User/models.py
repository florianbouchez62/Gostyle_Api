from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
import datetime
import os

class Promotion(models.Model):
    name = models.CharField("Name", max_length=255, unique=True)
    description = models.TextField("Description", max_length=1200)
    start_date = models.DateField('Start date', null=True)
    end_date = models.DateField('End date', null=True)
    percentage = models.FloatField("Percentage", default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    image = models.ImageField('Image', upload_to='Images',blank=True, null=True)
    qrcode = models.ImageField(upload_to='Qrcode', blank=True, null=True)
    active = models.BooleanField('Active ?', default=False)

    def clean(self):
        cleaned_data = super().clean()
        if self.start_date <= datetime.date.today():
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
    
    def delete_medias(self):
        try:
            os.remove(str(self.qrcode))
            os.remove(self.image.url)
        except:
            pass
