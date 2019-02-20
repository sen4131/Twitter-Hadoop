#!/home/training/anaconda3/bin/python3.6

# coding: utf-8

# # Twitter data

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import time
import tweepy
import pandas as pd
import json
import datetime


consumer_key = 
consumer_secret = 

access_token = 
access_token_secret = 

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#sets up the twitter stream
class MyStreamListener(StreamListener):
    def __init__(self, time_limit):
        self.start_time = time.time() #get the start time (in seconds)
        self.limit = time_limit
        self.saveFile = open('twitter_jobs.json', 'a')
        super(MyStreamListener, self).__init__()
 
    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:  #subtract the current time from the start time and check if it is less than the time limit
            self.saveFile.write(data)
            self.saveFile.write('\n')
            return True
        else:
            self.saveFile.close()
            return False

#get twitter data
myStream = Stream(auth, listener=MyStreamListener(time_limit=20))
myStream.filter(track=['Donald Trump'])

#clean file
tweets = pd.DataFrame() #Important info from tweets_data
tweets_data = [] #LIST OF DICT
output = 'output.txt' #append tweets to output

input_path = 'twitter_jobs.json'
#output_path = 'output.txt'

with open(input_path ,"r") as tweets_file:
    #x = f.readlines()
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    
#current tweet
tweets['created_at'] = list(map(lambda tweet: tweet.get('created_at', None),tweets_data))
tweets['id'] = list(map(lambda tweet: tweet.get('id', None),tweets_data))
tweets['text'] = list(map(lambda tweet: tweet.get('text', None),tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet.get('lang', None),tweets_data))
#tweets['reply_count'] = list(map(lambda tweet: tweet.get('reply_count', None),tweets_data))
#tweets['retweet_count'] = list(map(lambda tweet: tweet.get('retweet_count', None),tweets_data))
tweets['name'] = list(map(lambda tweet: tweet.get('user', {}).get('name',None) if tweet.get('user') != None else None,tweets_data))
tweets['userid'] = list(map(lambda tweet: tweet.get('user',{}).get('id',None),tweets_data))
tweets['location'] = list(map(lambda tweet: tweet.get('user', {}).get('location',None) if tweet.get('user') != None else None,tweets_data))
tweets['statuses_count'] = list(map(lambda tweet: tweet.get('user', {}).get('statuses_count',None) if tweet.get('user') != None else None,tweets_data))
tweets['createdate'] = pd.to_datetime(list(map(lambda tweet: tweet.get('user',{}).get('created_at',None),tweets_data)))
tweets['timedelta'] = (datetime.datetime.now()-tweets['createdate']).dt.days
tweets['rate'] = tweets['statuses_count']/tweets['timedelta']
tweets = tweets.replace('\n',' ', regex=True)
tweets = tweets.drop_duplicates(subset='id', keep='last')
tweets1 = tweets[tweets.text.str.contains("RT @") == False]


#write this to disc
path = "/flume/twitter/"
path2 = "/flume/twitter_rt/"
filename_prefix = "output"
filename_prefix2 = "output_rt"
filename_suffix = ".tsv"

currenttime = str(int(time.time()))

filename = path + filename_prefix + "_" + currenttime + filename_suffix
filename2 = path2 + filename_prefix2 + "_" + currenttime + filename_suffix

tweets1.to_csv(filename, sep='\t',index=False, header = False, encoding="utf-8")
tweets.to_csv(filename2, sep='\t',index=False, header = False, encoding="utf-8")



