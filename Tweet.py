# Connect twitter
# Search tweets
# Create tweet objects based on tweet data return them as an array
# repository link + example results + screencast - code overview and demo(2 searches)
# sadece ingilizce data alma eklenecek
# kaç data alınacak, hangi data alınacak
# uygulama sorsun hangi konu: datasize


# import tweepy
#
# auth = tweepy.OAuthHandler("DhfQ6430r0LgnBqHgsSXlwSbc", "HBQ65IK9q8bU6nOwDgRoMESo555xQSbhPWLCWUM7z8K7q2FVlw")
# auth.set_access_token("353853669-3Bs4DShz2k7XKdH66WJMSXymnSmBR4GwAR6IYekE", "VcaGuVxdslZ1JJTdiKRNhKmCw0ako73AOPET16YmN9OtD")
# api = tweepy.API(auth)
#
# fetched_tweets = api.search(q='Spotify', count=10)


class tw:

    def __init__(self,id, content, tweetDate):
        self.id = id
        self.content = content
        self.date = tweetDate
        self.sentimentScore = None


def getTweets(fetchedTweets):
    tweetArray = []
    id = 1
    for line in fetchedTweets:
        tweet = tw(id, line.text, line.created_at)
        tweetArray.append(tweet)
    return tweetArray


  



