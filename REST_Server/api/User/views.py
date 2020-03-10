
from django.shortcuts import render
from .serializers import PromotionSerializers
from .models import Promotion
from rest_framework import viewsets

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.filter(active=True).order_by('id')
    serializer_class = PromotionSerializers