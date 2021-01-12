import pandas as pd
import numpy as np
import analyzeKeywords as an
import matplotlib.pyplot as plt

import tweepy
import Tweet
import Sentiment


auth = tweepy.OAuthHandler("DhfQ6430r0LgnBqHgsSXlwSbc", "HBQ65IK9q8bU6nOwDgRoMESo555xQSbhPWLCWUM7z8K7q2FVlw")
auth.set_access_token("353853669-3Bs4DShz2k7XKdH66WJMSXymnSmBR4GwAR6IYekE", "VcaGuVxdslZ1JJTdiKRNhKmCw0ako73AOPET16YmN9OtD")
api = tweepy.API(auth)

fetched_tweets = api.search(q='Spotify', count=1000)
tweetFile =Tweet.getTweets(fetched_tweets)
array = []
for tweet in tweetFile:
    array.append(tweet.content)
resultP = an.get_most_used_words_by_type(array, "VRB")
print(resultP)


# df = pd.read_csv('test.csv')
#
# tweets = df['content'].tolist()
#
#
#
#
# # words in a list
# word_counts['words'] = word_counts.index
# word_counts.index = range(1, len(word_counts.index)+1)
# word_counts = word_counts[word_counts['words'].isin(['first', 'service', 'bug', 'buggy', 'freeze', 'slow', 'crash'])]
#
# print(word_counts)

