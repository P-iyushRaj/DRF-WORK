from django.contrib import admin

# Register your models here.
from .models import Total

@admin.register(Total)
class TotalAdmin(admin.ModelAdmin):
    list_display = ['id', 'total']