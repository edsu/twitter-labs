This is a little personal playground for working with the new Twitter Labs API.

To get started create generate your Twitter OAuth2 token.

    TWITTER_CONSUMER_KEY="changme" TWITTER_CONSUMER_SECRET="changme" ./key.py

This should have created a `config.py` file containing your token.

Now you can do a search:

    ./search.py obama > search.json

