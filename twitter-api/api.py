# -*- coding: utf-8 -*-

# tested with Python 3.4

import tweepy
import my_keys

# Set keys to variables. Note that they are imported from the my_keys.py file in the same folder
CONSUMER_KEY = my_keys.CONSUMER_KEY
CONSUMER_SECRET = my_keys.CONSUMER_SECRET
ACCESS_KEY = my_keys.ACCESS_KEY
ACCESS_SECRET = my_keys.ACCESS_SECRET

# Connect to API with the keys set above using the Tweepy library
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


###############
# Some things to try. Try uncommenting the lines with three hashes (###)
###############

# Print my account name

me = api.me().name
print(me)

# Update my status

### api.update_status(status="Look at me! I'm using APIs! #NYCDHWeek @Digital_Fellows @mkgold")

# Perform a search

### results = api.search(q="#NYCDHWeek")
### for result in results:
###     print('\n')
###     print(result.text)

# Write your search to a file (make sure the section above is uncommented)

### f = open('search.txt','w')
### for result in results:
###     f.write(result.text) 
### f.close()

