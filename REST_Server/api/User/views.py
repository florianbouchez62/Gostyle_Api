from django.shortcuts import render
from .serializers import ArticleSerializer, PromotionSerializers
from .models import Article, Promotion
from rest_framework import viewsets


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('id')
    serializer_class = ArticleSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all().order_by('id')
    serializer_class = PromotionSerializers