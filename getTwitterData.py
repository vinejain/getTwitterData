# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 01:21:07 2020

@author: Vineet PC
"""

import os
import tweepy as tw
import pandas as pd

consumer_key = "XMFPrO........h2AuqwhS"
consumer_secret = "aMUOs4Auwmt.....................9hvICk9vOz9cx9CZ7S"
access_token = "2799518809-4WJSkTyYKAN.....uSF7KggAyHEO91fWUcr1J4"
access_token_secret = "XLFH2BqFlcoME.............8C7pZI0frS9mgos2"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)


tweets = []
def username_tweets_to_csv(username,count):
    try: 
    # Pulling individual tweets from query
        for tweet in api.user_timeline(id=username, count=count):

            # Adding to list that contains all tweets
            tweets.append((tweet.created_at,tweet.id,tweet.text))

            # Creation of dataframe from tweets list
            tweetsdf = pd.DataFrame(tweets,columns=['Datetime', 'Tweet Id', 'Text'])

            # Converting dataframe to CSV
            tweetsdf.to_csv('{}-tweets.csv'.format(username)) 

    except BaseException as e:
          print('failed on_status,',str(e))
          time.sleep(3)
          
          
# Max recent tweets pulls x amount of most recent tweets from that user
username = 'LiveDrive'
count = 150

# Calling function to turn username's past X amount of tweets into a CSV file
username_tweets_to_csv(username, count)
os.getcwd()
