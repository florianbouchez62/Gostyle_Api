from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Promotion
import qrcode
import sys


@receiver(post_save, sender=Promotion)
def generate_qrcode(sender, instance, created, **kwargs) -> None:
    if created and 'test' not in sys.argv:
        qrcode_filename = 'qrcode_promotion_{}.png'.format(instance.pk)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('/promotions/{}/'.format(instance.pk))
        qr.make(fit=True)
        img = qr.make_image()
        img.save('media/Qrcodes/' + qrcode_filename)

        instance.qrcode = 'media/Qrcodes/' + qrcode_filename
        instance.save()
