from rest_framework import serializers

from .models import Article, Promotion


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'libelle', 'prix')

class PromotionSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promotion
        fields = ('id', 'article', 'pourcentage', 'qrCode')