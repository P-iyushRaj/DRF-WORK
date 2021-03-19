from django.contrib import admin

# Register your models here.
from .models import Tweet

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['id', 'tweet_id', 'published_date']