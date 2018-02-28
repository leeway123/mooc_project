# from django.contrib import admin
from teacher_app.models import *
import xadmin
# Register your models here.
xadmin.site.register(Teacher)
xadmin.site.register(Course)


