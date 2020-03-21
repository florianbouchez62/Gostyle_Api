from rest_framework import serializers

from .models import Promotion

class PromotionSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promotion
        fields = ('id', 'name', 'start_date', 'end_date', 'percentage', 'description')
