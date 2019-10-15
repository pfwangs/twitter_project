

import tweepy

#from tweepy import OAuthHandler
#from tweepy import Stream

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

    def filter(array):
        for item in array:
            item = item.lower()
            if 'the' in item:
                print(item)

    # create array of tweet information: username,
    # tweet id, date/time, text
    tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
    for j in tweets_for_csv:

        # Appending tweets to the empty array tmp
       tmp.append(j)
        #tmp = filter(track=['texas', 'usc', 'osu'])
        # Printing the tweets
    print(tmp)



# Driver code
if __name__ == '__main__':
    #l = StdOutListener()
    #auth = OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_key, access_secret)
    #stream = Stream(auth, l)
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.

    get_tweets("buhbuhbru")
    #stream.filter(track=['texas football', 'usc', 'osu'])