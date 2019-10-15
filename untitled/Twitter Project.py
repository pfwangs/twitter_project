

import tweepy

from html.parser import HTMLParser

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "Im7BpuDTwXVmJnj27oYVEztGT"
consumer_secret = "0YHZONwqL3v2V8fWC1BMagfW466LQgmZsIFkNaKJAHnwXoEYnd"
access_key = "55040175-oBon7B0xE2rBNYqtmdXCwQUmR67K9emzTR3yRgq8h"
access_secret = "hmsI5T9s9WWLr1Z1fWmyIRe1I5NW1U9rM67wZrW0wmX7f"

# Function to extract tweets
def get_tweets(username):

    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)

    # 200 tweets to be extracted

    number_of_tweets =200
    tmp = []
    tweets = api.user_timeline(screen_name=username)
    #tweet.filter(track=['texas', 'usc', 'osu'])
    for tweet in tweets:

        if tweet.lang == "en":
        #if 'texas' in currenttweet:
            tmp.append(tweet.text)
    filter(tmp)
    #return(tmp)
    #print(tmp)

def filter(array):
    for item in array:
        item = item.lower()
        if 'texas' in item:
            print(item)


# Driver code
if __name__ == '__main__':

    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.

    get_tweets("buhbuhbru")
