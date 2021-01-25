import pandas as pd
import analyzeKeywords as an


import tweepy
import Tweet
import Sentiment


# twitter authentication credentials
auth = tweepy.OAuthHandler("DhfQ6430r0LgnBqHgsSXlwSbc", "HBQ65IK9q8bU6nOwDgRoMESo555xQSbhPWLCWUM7z8K7q2FVlw")
auth.set_access_token("353853669-3Bs4DShz2k7XKdH66WJMSXymnSmBR4GwAR6IYekE", "VcaGuVxdslZ1JJTdiKRNhKmCw0ako73AOPET16YmN9OtD")
api = tweepy.API(auth)

# Get topic as input
topic = input('Enter topic for analysis: (e.g. microsoft word)\n')

# Use topic as filename prefix
keys = topic.split(' ')
file_name = ''
for i in keys:
    file_name = file_name + i + '_'

# Fetch tweets related to topic
fetched_tweets = api.search(q=topic, count=1000, lang='en')
tweet_list = Tweet.getTweets(fetched_tweets)

# Set sentiment scores of tweets
Sentiment.setSentiment(tweet_list)
Sentiment.exportCSV(tweet_list,file_name)

# Read sentiment csv and convert it to a data frame
df = pd.read_csv(file_name + 'sentiments.csv')

# Parse content column into a list
tweets = df['content'].tolist()

# Plot most used words
an.plot_most_used_words(tweets, file_name)

# Plot sentiment labels
an.plot_sentiments(df, file_name)

# Create word cloud
an.create_wordcloud(df, file_name)

# Filter tweets that contains domain keywords
an.tweets_with_keywords(df, file_name)
