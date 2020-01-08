This is a personal playground for working with the [Twitter Labs API]. The idea
is to hopefully inform future development of [twarc] rather than being useful in
itself.

To get started create generate your Twitter OAuth2 token.

    TWITTER_CONSUMER_KEY="changme" TWITTER_CONSUMER_SECRET="changme" ./key.py

This should have created a `config.py` file containing your token.

Now you can do a search:

    ./search.py obama > search.json

[Twitter Labs API]: https://developer.twitter.com/en/docs/labs/overview/introduction
[twarc]: https://twitter.com/docnow/twarc
