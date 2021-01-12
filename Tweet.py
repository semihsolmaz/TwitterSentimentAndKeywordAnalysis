# Connect twitter
# Search tweets
# Create tweet objects based on tweet data return them as an array

import tweepy



fetched_tweets = api.search(q='Qatar airways', count=10)

for tweet in fetched_tweets:
    print(tweet.text)


class tweet:
    def __init__(self, content, tweetDate):
        self.id = id()
        self.content = content
        self.date = tweetDate
        self.sentimentScore

