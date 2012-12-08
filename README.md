twitter-sentiment-graph
=======================

A microsite that analyzes the sentiment of a phrase on twitter and produces a graph.

## Prerequisites 

- PIP
- Python
- Flask
- python-twitter


## How to run

First things first is that you need to have some environment variables set up. You'll need to create your own Twitter account and register as developer to get these access keys. The environment variables must be named:

    TWITTER_CONSUMER_KEY
    TWITTER_CONSUMER_SECRET
    TWITTER_ACCESS_TOKEN
    TWITTER_ACCESS_TOKEN_SECRET

Run the command `python server.py` to start the server. Then go to [http://localhost:5000/](http://localhost:5000/) to see the app