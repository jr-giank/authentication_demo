from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser, Company

admin.site.unregister(Group)

admin.site.register(CustomUser)
admin.site.register(Company)