from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['tweet_id', 'tweet_text', 'published_date', 'is_active']

        