from rest_framework import serializers
from .models import Promotion
from django.core.files import File
import base64


class PromotionSerializers(serializers.HyperlinkedModelSerializer):
    
    base64_image = serializers.SerializerMethodField()

    class Meta:
        model = Promotion
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'percentage', 'base64_image')

    def get_base64_image(self, obj):
        try:
            f = open('Media/' + str(obj.image), 'rb')
            image = File(f)
            data = base64.b64encode(image.read())
            f.close()
            return data
        except:
            return ''

