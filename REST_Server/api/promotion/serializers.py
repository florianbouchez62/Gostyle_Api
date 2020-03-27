from rest_framework import serializers
from .models import Promotion
from django.core.files import File
import base64


class PromotionSerializers(serializers.HyperlinkedModelSerializer):

    base64_image = serializers.SerializerMethodField()

    class Meta:
        model = Promotion
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'percentage', 'base64_image')

    def get_base64_image(self, obj) -> str:
        try:
            with open('media/' + str(obj.image), 'rb') as open_image:
                image = File(open_image)
                data = base64.b64encode(image.read())
            return data
        except Exception:
            return ''
