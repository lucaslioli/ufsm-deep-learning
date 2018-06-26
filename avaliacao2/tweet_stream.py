import sys
import tweepy
import datetime

from authenticate import api_tokens

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    
    def on_status(self, status):
        print("-----------------------------------------")
        print("Language:", status.lang)
        print("Text:", status.text)

        tweet_insert = {}
        tweet_insert["text"]                  = status.text
        tweet_insert["lang"]                  = status.lang

        return True; # Don't kill the stream

    def on_error(self, status_code):
        print(sys.stderr, 'Encountered error with status code:' + str(status_code))
        print("-----------------------------------------")
        
        return True # Don't kill the stream

    def on_timeout(self):
        print(sys.stderr + 'Timeout...')
        print("-----------------------------------------")

        return True # Don't kill the stream

# Start the Stream Listener
def start_stream():
    print ("---------- STREAMING STARTED -----------")

    while True:
        try:
            myStream = tweepy.streaming.Stream(auth, MyStreamListener())
            myStream.filter(track=["a", "e", "i", "o", "u"], languages=["pt"])
        
        except ValueError:
            print('ERROR: Exeption occurred!' + ValueError)
            print("-----------------------------------------")
            
            continue



if __name__ == '__main__':
    # Variables that contains the user credentials to access Twitter API
    key = api_tokens()

    # Autenticação com a API Tweepy
    auth = tweepy.OAuthHandler(key['consumer_key'], key['consumer_secret'])
    auth.set_access_token(key['access_token'], key['access_token_secret'])

    # Autenticação com a API
    api = tweepy.API(auth)

    start_stream()