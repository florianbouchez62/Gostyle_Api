from django.contrib import admin
from django.contrib.auth.models import User

from .models import Promotion


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'start_date', 'end_date', 'percentage', 'image', 'active')
    exclude = ('qrcode',)