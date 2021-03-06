from django.db import models

# Create your models here.
class Tweet(models.Model):
    tweet_id = models.CharField(max_length=250, null=True, blank=True)
    tweet_text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.tweet_text

        