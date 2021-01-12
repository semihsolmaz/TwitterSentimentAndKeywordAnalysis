# Connect twitter
# Search tweets
# Create tweet objects based on tweet data return them as an array

import tweepy

auth = tweepy.OAuthHandler('dT8QrbTNl2Iv5RZ2vqqsSB4Ra', 'tpUB3N5MkrQ7tUwYSWpyQI90ytuz8WHyJVoCbZ5o2FlpUFRtEk')
auth.set_access_token('2483903256-UHDqrWSYTP28TOc5kzQNL3RH3xXJHTiUG3Y4sg1', 'tPSEJnQOwBwr4H1wK2UPZRqMWUAHANqaUrJLKYNjbemjI')

api = tweepy.API(auth)

fetched_tweets = api.search(q='Qatar airways', count=10)

for tweet in fetched_tweets:
    print(tweet.text)


class tweet:
    def __init__(self, content, tweetDate):
        self.id = id()
        self.content = content
        self.date = tweetDate
        self.sentimentScore

