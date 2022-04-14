from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(upload_file)
class UPLOAD_ADMIN(admin.ModelAdmin):
    list_display=['user','file','uploaded_at']