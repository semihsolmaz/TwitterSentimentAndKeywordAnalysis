import csv
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


def exportCSV(tweetList):
    csvFile = open('tweetList.csv', 'a')

    # create csv writer object
    csvWriter = csv.writer(csvFile)

    for tweet in tweetList:
        csvWriter.writerow(["id", "content", "tweetDate", "sentimentScore"])
        csvWriter.writerows(tweetList)

    csvFile.close()

    return tweetList

result = get_tweet_sentiment("super nice")
print(result)
