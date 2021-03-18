from django.contrib import admin

# Register your models here.
from .models import Cryptocurrency

@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'cryptocurrency']