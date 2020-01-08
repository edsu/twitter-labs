#!/usr/bin/env python3

# usage: key.py
#
# You should just need to run this once since it generates your OAuth2 token and
# saves it in config.py

import os
import json
import requests

consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET'] 
auth = (consumer_key, consumer_secret)
data = {'grant_type': 'client_credentials'}
url = "https://api.twitter.com/oauth2/token"

resp = requests.post(url, auth=auth, data=data).json()

code = 'TWITTER_KEY="{}"'.format(resp['access_token'])
open('config.py', 'w').write(code)
