import tweepy
import time

from authenticate import api_tokens
from tweet_stream import record

def download_tweets(file_name, sentiment):
    with open(file_name) as file:
        counter = 1
        for tweet_id in file:
            tweet_id = tweet_id.strip()

            try:
                tweet = api.get_status(tweet_id)

                tweet.text = tweet.text.replace('\n', ' ').replace('\r', '')
                record(sentiment+"_texts", tweet.text, tweet.id)

                print(str(counter), "- Tweet:", tweet.id, "recorded")

            except tweepy.error.TweepError:
                print(str(counter), "- Tweet:", tweet_id, "is not available")

            counter += 1
            time.sleep(0.5)

if __name__ == '__main__':
    # Variables that contains the user credentials to access Twitter API
    key = api_tokens()

    # Tweepy API authentication
    auth = tweepy.OAuthHandler(key['consumer_key'], key['consumer_secret'])
    auth.set_access_token(key['access_token'], key['access_token_secret'])

    # API authentication
    api = tweepy.API(auth)

    with open("files/positive_texts.txt", 'w') as f:
        f.write("")

    with open("files/positive_texts.pkl", 'w') as f:
        f.write("")

    print("Extraction positive tweets ...")
    download_tweets("files/positive_tweets.txt", "positive")

    print("Extrating negative tweets ...")
    download_tweets("files/negative_tweets.txt", "negative")

    print("End")
