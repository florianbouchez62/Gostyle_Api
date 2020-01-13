from django.contrib import admin
from django.contrib.auth.models import User

from .models import Article, Promotion


# Register your models here.

admin.site.register(Article)
admin.site.register(Promotion)