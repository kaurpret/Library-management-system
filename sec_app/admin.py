from django.contrib import admin
from . models import *
# Register your models here.
class stu(admin.ModelAdmin):
    list_display = ('first_name','last_name','class_name')
admin.site.register(student,stu)
