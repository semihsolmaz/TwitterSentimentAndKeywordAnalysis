import pandas as pd
from textblob import TextBlob
import tweepy
import analyzeKeywords

tweetList = []

def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(analyzeKeywords.clean_tweet(tweet))
    # set sentiment
    return analysis.sentiment.polarity


def setSentiment(tweetList):
    for tweet in tweetList:
        tweet.sentimentScore = get_tweet_sentiment(tweet.content)


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
