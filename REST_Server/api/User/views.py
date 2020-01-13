from django.shortcuts import render
from .serializers import ArticleSerializer
from .models import Article
from rest_framework import viewsets


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('libelle')
    serializer_class = ArticleSerializer
