import tweepy
from tweepy.auth import OAuthHandler
from .models import Tweet

ConsumerKey  = '99CU3AtOt9HcbzybPPeWhn1Ka'
ConsumerSecret = 'u3EBMm5ptJE0pAoa3aoq2umsgtGbX08c5FlI64wI8XZ8bXpRrZ'
OAuthAccessToken = '4190585592-h1xPB02HRZGzIzU4egn1M8U3M9XkkDNEpwAlOIW'
OAuthAccessTokenSecret = 'vcfZ3M3ajXvar3qmS5aypeSlCPDJfdjVzOR4Eve3TQUKX'
#BearerToken = 'AAAAAAAAAAAAAAAAAAAAAAwVNwEAAAAA4E%2BSonkXQ8fFBiS2fNRRB5AQgJ4%3DUXWmgS9QuTVqzaZ49775isqwwpIAZK91rpwzrfqBva51zWWkXt'

def user_tweets():
    auth = OAuthHandler( ConsumerKey, ConsumerSecret )
    auth.set_access_token( OAuthAccessToken, OAuthAccessTokenSecret )
    #breakpoint()
    api = tweepy.API(auth)
    user_tweets = api.user_timeline(count=10)
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

