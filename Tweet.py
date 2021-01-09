# Connect twitter
# Search tweets
# Create tweet objects based on tweet data return them as an array

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


class tweet:
    def __init__(self, content, tweetDate):
        self.id = id()
        self.content = content
        self.date = tweetDate
        self.sentimentScore

