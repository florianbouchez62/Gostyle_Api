from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from .middleware import get_request
from django.db import models
import datetime
import os
import qrcode
import json


class Promotion(models.Model):
    code = models.CharField("Promotion code", max_length=255, unique=True)
    description = models.TextField("Description", max_length=1200)
    start_date = models.DateField('Start date')
    end_date = models.DateField('End date')
    percentage = models.FloatField("Percentage", default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    image = models.ImageField('Image', upload_to='Images', blank=True, null=True)
    qrcode = models.ImageField(upload_to='Qrcode', blank=True, null=True)
    active = models.BooleanField('Active ?', default=False)

    def get_promotion_name(self) -> str:
        return self.name

    def get_promotion_percentage(self) -> float:
        return self.percentage

    def get_promotion_active(self) -> bool:
        return self.active

    def __repr__(self) -> str:
        return self.name + " added."

    def clean(self) -> None:
        cleaned_data = super().clean()
        if self.start_date <= datetime.date.today():
            raise ValidationError('The start date must be greater than the current date.')
        if self.start_date >= self.end_date:
            raise ValidationError('The end date must be greater than the start date.')
        if self.active:
            if not self.image:
                raise ValidationError('Image is missing to activate the promotion. You must uncheck the active\
                                        checkbox or be sure to have image.')

        return cleaned_data

    def delete_medias(self) -> None:
        try:
            os.remove(self.image.url)
            os.remove(str(self.qrcode))
        except Exception:
            pass

    def generate_qrcode(self) -> None:
        qrcode_filename = 'qrcode_promotion_{}.png'.format(self.pk)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        application_user = User.objects.get(username="Application")
        if application_user:
            token, token_created = Token.objects.get_or_create(user=application_user)
            data = {'token': token.key, 'url': '/promotions/{}/'.format(self.pk)}
            qr.add_data(json.dumps(data))
            qr.make(fit=True)
            img = qr.make_image()
            img.save('media/Qrcodes/' + qrcode_filename)
            self.qrcode = 'media/Qrcodes/' + qrcode_filename
            self.save()
