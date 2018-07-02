import re
import numpy as np
import pickle as pkl
import string                                   # Remove the ponctuation from the texts
import unicodedata                              # Remove the accents from the texts
from nltk.corpus import stopwords               # Methods to remove stop words
from nltk.stem.wordnet import WordNetLemmatizer # Methods to lemmatize the texts
from tweet_stream import record                 # Records the processed texts into a file

def pickleLoader(pklFile):
    try:
        while True:
            yield pkl.load(pklFile)
    except EOFError:
        pass

if __name__ == '__main__':
    # Clears the file
    with open("files/processed_tweets.txt", 'w') as f:
        f.write("")

    with open("files/processed_tweets.pkl", 'w') as f:
        f.write("")

    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+", flags=re.UNICODE)

    # Getting the set of stop words
    stop = set(stopwords.words('portuguese'))

    # Getting the set of punctuation
    pont=set(string.punctuation)

    # Instance an object lemmatizer
    lemma = WordNetLemmatizer()

    with open("files/unprocessed_tweets.pkl", 'rb') as f:
        for text in pickleLoader(f):
            print("ORIGINAL:", text)

            # To make the text minuscule
            text = text.lower()

            # To remove URLs, mentions and hashtags from the text
            text = re.sub(r'http\S+|@\S+|#\S+', '', text)

            # To remove the emojis from the text
            text = emoji_pattern.sub(r'', text)

            # To remove the stop words from the text
            text = ' '.join([w for w in text.split() if w not in stop])

            # To remove the ponctuation from the text
            text = ''.join(ch for ch in text if ch not in pont)

            # Lemmatizes the text
            text = ' '.join(lemma.lemmatize(w) for w in text.split())

            # To remove the accents from the text
            text = ''.join(c for c in unicodedata.normalize('NFD', text)
                  if unicodedata.category(c) != 'Mn')

            # To remove duplicate letters - STAND BY
            # text = re.sub(r'(\w)\1+', r'\1', text)

            # To remove the white spaces in the beginning and in the end of the text
            text = text.lstrip().rstrip()

            print("PROCESSED:", text, "\n")

            record("processed_tweets", text);