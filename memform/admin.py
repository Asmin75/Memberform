from django.contrib import admin
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth
from .models import Member


admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
admin.site.register(Member)
# Register your models here.
