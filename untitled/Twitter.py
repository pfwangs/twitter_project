from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream



access_token = "55040175-oBon7B0xE2rBNYqtmdXCwQUmR67K9emzTR3yRgq8h"
access_token_secret = "hmsI5T9s9WWLr1Z1fWmyIRe1I5NW1U9rM67wZrW0wmX7f"
consumer_key = "Im7BpuDTwXVmJnj27oYVEztGT"
consumer_secret = "0YHZONwqL3v2V8fWC1BMagfW466LQgmZsIFkNaKJAHnwXoEYnd"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['texas', 'usc', 'osu'])



