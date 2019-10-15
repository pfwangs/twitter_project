
import tweepy

from tweepy import StreamListener
from tweepy import Stream



# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "Im7BpuDTwXVmJnj27oYVEztGT"
consumer_secret = "0YHZONwqL3v2V8fWC1BMagfW466LQgmZsIFkNaKJAHnwXoEYnd"
access_key = "55040175-oBon7B0xE2rBNYqtmdXCwQUmR67K9emzTR3yRgq8h"
access_secret = "hmsI5T9s9WWLr1Z1fWmyIRe1I5NW1U9rM67wZrW0wmX7f"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)
# Function to extract tweets



# Driver code
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    stream = Stream(auth, l)
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.


    stream.filter(follow = ['575930104'])



