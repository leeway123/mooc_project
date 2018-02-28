from django.contrib import admin
from .models import UserProfile
import xadmin
# Register your models here.
xadmin.site.register(UserProfile)

