import pandas as pd
import re
import nltk
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud


# looks for specific words in a text returns true if text contains that word
def contain_related_word(text):
    look_up_words = ['bug', 'buggy', 'freeze', 'slow', 'crash', 'glitch', 'slowness', 'frozen', 'broken',
                     'error', 'frustrating', 'frustration']
    tokens = nltk.word_tokenize(text)
    t = [x in tokens for x in look_up_words]
    if True in t:
        return True
    else:
        return False


# filters the csv file that contains tweets and created another csv file that only containstweets that have
# related words
def tweets_with_keywords(df, file_name):
    mask = df['content'].apply(contain_related_word)
    tweets_with_keys = df[mask]
    tweets_with_keys.to_csv(file_name + 'tweets_with_keywords.csv')


# helper function to clean tweets from punctuation, mentions, stopwords etc.
def clean_tweet(tweet, search_terms=''):
    search_items = search_terms.split('_')
    stop_words = stopwords.words('english')
    stop_words.append('rt')
    for item in search_items:
        stop_words.append(item)
    cleaned = (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet).split())).lower()
    words = cleaned.split(' ')
    no_stop = []
    for word in words:
        if word not in stop_words:
            no_stop.append(word)
        clean_string = ' '.join(no_stop)
    return clean_string


# Creates a word cloud using tweet texts
def create_wordcloud(df, file_name):
    tweets_str = ''
    for line in df['content']:
        line = str(line)
        tweets_str = tweets_str + clean_tweet(line, file_name)
    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          min_font_size=10).generate(tweets_str)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.savefig(file_name + "wordcloud.pdf", bbox_inches='tight')

# get most used words by word types such as noun, adj, etc
# gets nltk word type str as input
def get_most_used_words_by_type(fetched_tweets, word_type, search_str):
    tweet_words_list = []
    for tweet in fetched_tweets:
        tokens = nltk.word_tokenize(clean_tweet(tweet, search_str))
        text = nltk.Text(tokens)
        tags = nltk.pos_tag(text)
        filtered = filter(lambda tag: tag[1] == word_type, tags)
        for word in filtered:
            tweet_words_list.append(word[0])

    counts = Counter(tweet_words_list)
    return counts


# get most used words by count
def get_most_used_words(fetched_tweets, search_str):
    tweet_words_list = []
    for tweet in fetched_tweets:
        tokens = nltk.word_tokenize(clean_tweet(tweet, search_str))
        text = nltk.Text(tokens)
        for word in tokens:
            tweet_words_list.append(word)
    counts = Counter(tweet_words_list)
    return counts


# Labels sentiments as negative, positive and neutral
def label_sentiment(sentiment):
    if sentiment < 0:
        return 'negative'
    elif sentiment > 0:
        return 'positive'
    else:
        return 'neutral'


# Returns date time
def get_date(datetime):
    return datetime[:10]


# Reads sentiment labels from csv creates a plot and saves as a pdf
def plot_sentiments(tweet_list_df, file_name):
    tweet_list_df['Sentiment'] = tweet_list_df['sentimentScore'].apply(lambda row: label_sentiment(row))
    tweet_list_df['date'] = tweet_list_df['date'].apply(lambda row: get_date(row))
    tweet_list_df.groupby(['date', 'Sentiment']).size().plot.bar(y='counts')
    print(tweet_list_df['date'][0])
    plt.savefig(file_name + "sentiments.pdf", bbox_inches='tight')


# Reads text of csv counts words and plots word counts, saves plot as csv
def plot_most_used_words(tweets, file_name):
    word_count = get_most_used_words(tweets, file_name)
    word_counts = pd.DataFrame.from_dict(word_count,orient='index',columns=['counts']).sort_values('counts', ascending=False).head(20)
    count_graph = word_counts['counts'].plot.bar(y='counts', rot=90)
    plt.savefig(file_name + "most_used_words.pdf", bbox_inches='tight')

