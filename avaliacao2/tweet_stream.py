import sys
import tweepy
import pickle

from authenticate import api_tokens

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    
    def on_status(self, status):
        print("-----------------------------------------")
        print("Language:", status.lang)
        print("Text:", status.text)

        status.text = status.text.replace('\n', ' ').replace('\r', '')
        record(status.text)

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

def record(msg = ""):
    with open("text-part1.pck", 'ab') as pck:
        pickle.dump(msg, pck, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    # Variables that contains the user credentials to access Twitter API
    key = api_tokens()

    # Autenticação com a API Tweepy
    auth = tweepy.OAuthHandler(key['consumer_key'], key['consumer_secret'])
    auth.set_access_token(key['access_token'], key['access_token_secret'])

    # Autenticação com a API
    api = tweepy.API(auth)

    start_stream()

    f = open('text-part-1.csv','a')
    f.write(str(now) + " = " + message + '\n')
    f.close()