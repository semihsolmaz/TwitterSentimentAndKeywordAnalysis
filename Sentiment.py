import tweepy
import csv
from textblob import TextBlob

import nltk
from nltk.corpus import stopwords

tweetList = []


def setSentiment(tweetList):
    analysis = TextBlob(tweetList).sentiment
    print(analysis)

    return tweetList


def exportCSV(tweetList):
    csvFile = open(tweetList.csv, 'a')

    csvWriter = csv.writer(csvFile)

    for tweet in tweetList:
        csvWriter.writerow(["id", "content", "tweetDate"])
        csvWriter.writerows(tweetList)

    return exportCSV(tweetList)