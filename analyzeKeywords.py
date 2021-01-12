import pandas as pd
import numpy as np
import re
import tweepy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
import matplotlib.pyplot as plt



def contain_related_word(text):
    look_up_words = ['bug', 'buggy', 'freeze', 'slow', 'crash']
    tokens = text.split()
    t = [x in tokens for x in look_up_words]
    if True in t:
        return True
    else:
        return False


def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


# auth = tweepy.OAuthHandler('dT8QrbTNl2Iv5RZ2vqqsSB4Ra', 'tpUB3N5MkrQ7tUwYSWpyQI90ytuz8WHyJVoCbZ5o2FlpUFRtEk')
# auth.set_access_token('2483903256-UHDqrWSYTP28TOc5kzQNL3RH3xXJHTiUG3Y4sg1', 'tPSEJnQOwBwr4H1wK2UPZRqMWUAHANqaUrJLKYNjbemjI')
#
# api = tweepy.API(auth)
#
# fetched_tweets = api.search(q='Qatar airways', count=200)
def get_most_used_words_by_type(fetched_tweets, word_type):
    tweet_words_list = []
    for tweet in fetched_tweets:
        tokens = nltk.word_tokenize(clean_tweet(tweet))
        text = nltk.Text(tokens)
        tags = nltk.pos_tag(text)
        filtered = filter(lambda tag: tag[1] == word_type, tags)
        for word in filtered:
            tweet_words_list.append(word[0])

    counts = Counter(tweet_words_list)
    return counts


# dist = get_most_used_words(fetched_tweets, 'NN')
def get_most_used_words(fetched_tweets):
    tweet_words_list = []
    for tweet in fetched_tweets:
        tokens = nltk.word_tokenize(clean_tweet(tweet))
        text = nltk.Text(tokens)
        for word in tokens:
            tweet_words_list.append(word)
    counts = Counter(tweet_words_list)
    return counts

def get_words_by_sentiment(tweets, sentiment):
    tweet_words_list = []
    for tweet in tweets:
        tokens = nltk.word_tokenize(clean_tweet(tweet.text))
        text = nltk.Text(tokens)
        for token in text:
            tweet_words_list.append(token)
    sid = SentimentIntensityAnalyzer()
    pos_word_list = []
    neu_word_list = []
    neg_word_list = []

    for word in tweet_words_list:
        if (sid.polarity_scores(word)['compound']) >= 0.5:
            pos_word_list.append(word)
        elif (sid.polarity_scores(word)['compound']) <= -0.5:
            neg_word_list.append(word)
        else:
            neu_word_list.append(word)
    if sentiment == 'pos':
        return pos_word_list
    elif sentiment == 'neg':
        return neg_word_list
    elif sentiment == 'neu':
        return neu_word_list
    else:
        print('invalid sentiment')


def plot_most_used_words(tweets):
    word_count = get_most_used_words(tweets)

    # words in count
    word_counts = pd.DataFrame.from_dict(word_count,orient='index',columns=['counts']).sort_values('counts', ascending=False).head(20)
    count_graph = word_counts['counts'].plot.bar(y='counts', rot=90)
    plt.show()


def plot_related_word_count(tweets):
    word_count = get_most_used_words(tweets)
    word_counts = pd.DataFrame.from_dict(word_count,orient='index',columns=['counts']).sort_values('counts', ascending=False)
    word_counts['words'] = word_counts.index
    word_counts.index = range(1, len(word_counts.index) + 1)
    word_counts = word_counts[word_counts['words'].isin(['first', 'service', 'bug', 'buggy', 'freeze', 'slow', 'crash'])]
    plt.show()

# neg_words = get_words_by_sentiment(fetched_tweets, 'pos')

# tweet_list = []
# for tweet in fetched_tweets:
#     tweet_list.append(tweet.text)

# r = contain_related_word('we have a freeze')
# # print(r)
# arr = np.array(tweet_list)
# tweets = pd.read_csv('test.csv')
# print(tweets['content'])
# word_filter = tweets['content'].apply(contain_related_word)
# print(word_filter)
# print(tweets[word_filter])
# df = pd.DataFrame(arr, columns=['content'])
#
# df.to_csv('sample.csv')


# Read csv

# get most used words

# Find related words

# Create report and graph

