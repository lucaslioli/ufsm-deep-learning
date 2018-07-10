import sys
import tweepy
import pickle as pkl

from authenticate import api_tokens

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if(not status.retweeted and 'RT @' not in status.text[0:4] and status.lang == "pt"):
            print("-----------------------------------------")
            print("Lang:", status.lang)
            print("Text:", status.text)

            status.text = status.text.replace('\n', ' ').replace('\r', '')

            record("unprocessed_tweets", status.text, status.id)

        return True; # Don't kill the stream

    def on_error(self, status_code):
        print('Encountered error with status code:', status_code)
        print("-----------------------------------------")

        return True # Don't kill the stream

    def on_exception(self, exception):
        print('Exception: ', exception)
        print("-----------------------------------------")

        return True # Don't kill the stream

    def on_timeout(self, timeout):
        print('Timeout: ', timeout)
        print("-----------------------------------------")

        return True # Don't kill the stream

# Start the Stream Listener
def start_stream():
    print ("---------- STREAMING STARTED -----------")

    while True:
        try:
            myStream = tweepy.streaming.Stream(auth, MyStreamListener())
            myStream.filter(track=["a", "e", "i", "o", "u"], stall_warnings=True)

        except ValueError:
            print('ERROR: Exeption occurred!' + ValueError)
            print("-----------------------------------------")

            continue

# Records the tweet ID and message into a file
def record(file_name, msg, id = ""):
    # Using a txt file for testing purposes
    with open("files/"+file_name+".txt", 'a') as f:
        if(id != ""):
            f.write(str(id) + " => " + msg + '\n')
        else:
            f.write(msg + '\n')

    with open("files/"+file_name+".pkl", 'ab') as f:
        pkl.dump(msg, f, pkl.HIGHEST_PROTOCOL)

# Records the tweet ID and message into a file
def record_array(file_name, arr):
    # Using a txt file for testing purposes
    with open("files/"+file_name+".txt", 'a') as f:
        f.write(arr[0] + ", " + arr[1] + '\n')

    with open("files/"+file_name+".pkl", 'ab') as f:
        pkl.dump(arr, f, pkl.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    # Variables that contains the user credentials to access Twitter API
    key = api_tokens()

    # Tweepy API authentication
    auth = tweepy.OAuthHandler(key['consumer_key'], key['consumer_secret'])
    auth.set_access_token(key['access_token'], key['access_token_secret'])

    # API authentication
    api = tweepy.API(auth)

    start_stream()