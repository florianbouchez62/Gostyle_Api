from .serializers import PromotionSerializers
from .models import Promotion
from rest_framework import viewsets, permissions


class PromotionViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head']
    queryset = Promotion.objects.filter(active=True).order_by('id')
    serializer_class = PromotionSerializers
