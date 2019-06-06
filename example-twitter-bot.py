import re
import requests
import json
import time

import tweepy
#from secrets import *

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

lastTime = 0

baseUrl = "http://corpus-db.org"
for i in range(109,50000):
    print('Getting text with id: %s' % i)
    metaResponse = requests.get('http://corpus-db.org/api/id/' + str(float(i)))
    if metaResponse.ok:
        metaParsed = json.loads(metaResponse.text)
        if 'title' in metaParsed: 
            print('Title: ', metaParsed['title'])
        else: 
            print('No title found.')
    else: 
        print("Couldn't get metadata for id: %s" % i)
        continue
    textResponse = requests.get('http://corpus-db.org/api/id/' + str(float(i)) + '/fulltext')
    if textResponse.ok:
        textParsed = json.loads(textResponse.text)
        if len(textParsed) > 0: 
            text = textParsed[0]['text'] if 'text' in textParsed[0] else ''
            text = text.replace('\n', ' ')
            matches = re.findall('\s([Dd]\w+\s[Hh]\w+\s[Ss]\w+\s[Ii]\w+)\s\w+', text, re.MULTILINE)
            print('--------------- FOUND ----------------')
            for match in matches: 
                timeSinceLast = time.time() - lastTime
                while timeSinceLast < 3600: 
                    print('Waiting...') 
                    timeSinceLast = time.time() - lastTime
                    time.sleep(500)
                tweet = "DHSI also stands for: \"" + match + "\" as found in " + metaParsed['title']
                tweet += ". See http://gutenberg.org/ebooks/%s for the full text. #DHSI19" % i
                print(tweet)
                try:
                    api.update_status(tweet)
                except:
                    print('Twitter error. Skipping.')
                    continue
                lastTime = time.time()
        else: 
            print('No text here.')
    else:
        print("Couldn't get full text!")
        continue
