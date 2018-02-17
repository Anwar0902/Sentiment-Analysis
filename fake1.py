from nltk.tokenize import sent_tokenize
from tweepy import Stream
from tweepy.streaming import StreamListener
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tweepy import Stream, OAuthHandler
import json
import time
import requests
import datetime

consumer_key = '***************'
consumer_secret = '**************'
access_token = '****************'
access_secret = '*********'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
#API_ENDPOINT = "http://pastebin.com/api/api_post.php"
#api = tweepy.API(auth)
sent = 0.0
count = 0
class MyListener(StreamListener):
 
    def on_data(self, data):
        global count
        global sent
        try:
            sid = SentimentIntensityAnalyzer()
            tweet = json.loads(data)
            tweet =tweet["text"]
            print(tweet)
            sentList = sent_tokenize(tweet)

            # Go through each sentence in tweet
            for sentence in sentList:
                count += 1
                ss = sid.polarity_scores(sentence)
                sent += ss['compound']  # Tally up the overall sentiment
            if(count!=0):
                print(sent/count)
                print(count)
        except BaseException as e:
            print('Failed: ', str(e))
            time.sleep(1)
        #print(sent)

    def on_error(self, status):
        print('Error: ', status)
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['padmavat'])
#abachgxz123
# Update the sentiment

