# Connect twitter
# Search tweets
# Create tweet objects based on tweet data return them as an array
# repository link + example results + screencast - code overview and demo(2 searches)
# sadece ingilizce data alma eklenecek
# kaç data alınacak, hangi data alınacak
# uygulama sorsun hangi konu: datasize


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


  



