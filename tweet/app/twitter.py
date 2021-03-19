import tweepy
from tweepy.auth import OAuthHandler
from .models import Tweet

ConsumerKey  = 'LdWeCQV9McfbiD9ypEwYNDH0k'
ConsumerSecret = 'jcH3fjLQJ4VcSLAvfvr8i4Cm3nJz9yzItIA4IHGBZGFaL0aQ3m'
OAuthAccessToken = '4190585592-nnGEwj1vXxVPy3bI7s5gfLdGc6ELBMt49HFYNmJ'
OAuthAccessTokenSecret = 'xlNbpxPDTwkNNUinUg7CIlmCcci2PPRjHGurzb0eGoQrC'
#BearerToken = 'AAAAAAAAAAAAAAAAAAAAAAwVNwEAAAAA4E%2BSonkXQ8fFBiS2fNRRB5AQgJ4%3DUXWmgS9QuTVqzaZ49775isqwwpIAZK91rpwzrfqBva51zWWkXt'

def user_tweets():
    auth = OAuthHandler('ConsumerKey', 'ConsumerSecret')
    auth.set_access_token('OAuthAccessToken', 'OAuthAccessTokenSecret')
    api = tweepy.API(auth)
    user_tweets = api.user_timeline(count=20)
    return user_tweets

def save_to_db():
    original_tweets = user_tweets()
    for original_tweet in original_tweets:
        if not original_tweet.retweeted:
            if not Tweet.objects.filter(tweet_id=original_tweet.id):
                new_tweet = Tweet(tweet_id = original_tweet.id, tweet_text = original_tweet.text, published_date = original_tweet.created_at, is_active = True)
                new_tweet.save()

def set_inactive(pk):
    Tweet.objects.filter(tweet_id = pk).update(is_active = False)

def set_active(pk):
    Tweet.objects.filter(tweet_id = pk).update(is_active = True)

