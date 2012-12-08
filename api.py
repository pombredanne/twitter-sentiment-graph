import twitter
import os

consumer_key=os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret=os.environ.get("TWITTER_CONSUMER_SECRET")
access_key=os.environ.get("TWITTER_ACCESS_TOKEN")
access_key_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_key,
                      access_token_secret=access_key_secret)
                      


def getTweets(query=None):
    return map((lambda tweet: tweet.AsDict()), api.GetSearch(term='NHL'))