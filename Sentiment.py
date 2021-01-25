import pandas as pd
from textblob import TextBlob
import analyzeKeywords


# Get sentient score of a given text
def get_tweet_sentiment(tweet):
    # create TextBlob object of passed tweet text
    analysis = TextBlob(analyzeKeywords.clean_tweet(tweet))
    # set sentiment
    return analysis.sentiment.polarity


# Sets sentiment score of a tweet object
def setSentiment(tweetList):
    for tweet in tweetList:
        tweet.sentimentScore = get_tweet_sentiment(tweet.content)


# Saves tweets object list to a csv file
def exportCSV(tweet_list, file_name):
    idArr = []
    contentArr = []
    dateArr = []
    sentimentArr = []
    for tweet in tweet_list:
        idArr.append(tweet.id)
        contentArr.append(tweet.content)
        dateArr.append(tweet.date)
        sentimentArr.append(tweet.sentimentScore)
    dict = {"content": contentArr, "date":dateArr, "sentimentScore": sentimentArr}
    frame = pd.DataFrame(dict)
    frame.to_csv(file_name + "sentiments.csv")
