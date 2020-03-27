from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import Promotion
from django.conf import settings
from django.core.files import File
import qrcode
import sys
import os, glob

@receiver(post_save, sender=Promotion)
def generate_qrcode(sender, instance, created, **kwargs):
    if created and not 'test' in sys.argv:
        filename = 'qrcode_promotion_{}.png'.format(instance.pk)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('/promotions/{}/'.format(instance.pk))
        qr.make(fit=True)
        img = qr.make_image()
        img.save('Media/Qrcodes/' + filename)

        instance.qrcode = 'Media/Qrcodes/' + filename
        instance.save()
