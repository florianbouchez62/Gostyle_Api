from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
import datetime
import os


class Promotion(models.Model):
    name = models.CharField("Name", max_length=255, unique=True)
    description = models.TextField("Description", max_length=1200)
    start_date = models.DateField('Start date')
    end_date = models.DateField('End date')
    percentage = models.FloatField("Percentage", default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    image = models.ImageField('Image', upload_to='Images', blank=True, null=True)
    qrcode = models.ImageField(upload_to='Qrcode', blank=True, null=True)
    active = models.BooleanField('Active ?', default=False)

    def clean(self) -> None:
        cleaned_data = super().clean()
        if self.start_date <= datetime.date.today():
            raise ValidationError('The start date must be greater than the current date.')
        if self.start_date >= self.end_date:
            raise ValidationError('The end date must be greater than the start date.')
        if self.active:
            if self.pk and self.check_empty_fields():
                raise ValidationError('Image or qrcode ( maybe both ) is missing to activate the promotion.\
                                       You must uncheck the active checkbox or be sure to have both\
                                       image and qrcode.')
            elif not self.image:
                raise ValidationError('Image is missing to activate the promotion. You must uncheck the active\
                                        checkbox or be sure to have both image and qrcode.')

        return cleaned_data

    def check_empty_fields(self) -> bool:
        if not os.path.isfile(str(self.qrcode)) or not self.image:
            return True
        return False

    def get_promotion_name(self) -> str:
        return self.name

    def get_promotion_percentage(self) -> float:
        return self.percentage

    def get_promotion_active(self) -> bool:
        return self.active

    def __repr__(self) -> str:
        return self.name + " added."

    def delete_medias(self) -> None:
        try:
            os.remove(self.image.url)
            os.remove(str(self.qrcode))
        except Exception:
            pass