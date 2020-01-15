from django.contrib import admin
from django.contrib.auth.models import User

from .models import Promotion


# Register your models here.

admin.site.register(Promotion)