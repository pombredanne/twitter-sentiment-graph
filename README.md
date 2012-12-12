twitter-sentiment-graph
=======================

A microsite that analyzes the sentiment of a phrase on twitter and produces a graph.

## Prerequisites 

- PIP
- Python
- Flask
- python-twitter

## Installation

First you need to make sure that you have the [Flask](http://flask.pocoo.org/) web framework installed.

    pip install flask
    
Next you need to have python-twitter installed.

    pip install python-twitter

Then you'll need to set up the following environment variables.

    TWITTER_CONSUMER_KEY
    TWITTER_CONSUMER_SECRET
    TWITTER_ACCESS_TOKEN
    TWITTER_ACCESS_TOKEN_SECRET


## How to run

Run the command `python server.py` to start the server. Then go to [http://localhost:5000/](http://localhost:5000/) to see the app