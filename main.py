import pandas as pd
import analyzeKeywords as an


import tweepy
import Tweet
import Sentiment




auth = tweepy.OAuthHandler("DhfQ6430r0LgnBqHgsSXlwSbc", "HBQ65IK9q8bU6nOwDgRoMESo555xQSbhPWLCWUM7z8K7q2FVlw")
auth.set_access_token("353853669-3Bs4DShz2k7XKdH66WJMSXymnSmBR4GwAR6IYekE", "VcaGuVxdslZ1JJTdiKRNhKmCw0ako73AOPET16YmN9OtD")
api = tweepy.API(auth)

topic = input('Enter topic for analysis: (e.g. microsoft word)\n')
keys = topic.split(' ')
file_name = ''
for i in keys:
    file_name = file_name + i + '_'

fetched_tweets = api.search(q=topic, count=1000, lang='en')
tweet_list = Tweet.getTweets(fetched_tweets)

Sentiment.setSentiment(tweet_list)
Sentiment.exportCSV(tweet_list,file_name)

# array = []
# for tweet in tweetFile:
#     array.append(tweet.content)
# resultP = an.get_most_used_words_by_type(array, "VRB")
# print(resultP)


df = pd.read_csv(file_name + 'sentiments.csv')

tweets = df['content'].tolist()

an.plot_most_used_words(tweets, file_name)
an.plot_sentiments(df, file_name)

an.create_wordcloud(df, file_name)

an.tweets_with_keywords(df, file_name)

samp = 'I have bug in me'
print(an.contain_related_word(samp))

# # words in a list
# word_counts['words'] = word_counts.index
# word_counts.index = range(1, len(word_counts.index)+1)
# word_counts = word_counts[word_counts['words'].isin(['first', 'service', 'bug', 'buggy', 'freeze', 'slow', 'crash'])]
#
# print(word_counts)

