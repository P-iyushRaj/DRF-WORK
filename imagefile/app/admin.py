from django.contrib import admin

# Register your models here.
from .models import Notes

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']