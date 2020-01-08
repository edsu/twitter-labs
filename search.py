#!/usr/bin/env python

# usage: ./search.py obama > results.json

import sys
import json
import config
import requests

url = 'https://api.twitter.com/labs/1/tweets/search'
headers = {'Authorization': 'Bearer {}'.format(config.TWITTER_KEY)}

params = {
    'query': sys.argv[1],
    'format': 'detailed',
    'expansions': 'attachments.poll_ids,attachments.media_keys,author_id,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id'
}

data = requests.get(url, params=params, headers=headers).json()
print(json.dumps(data, indent=2))
