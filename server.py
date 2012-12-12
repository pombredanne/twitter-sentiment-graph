from flask import Flask
from flask import render_template
from api import getTweets
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sentiment/<search>")
def sentiment(search):
    results = getTweets(search)
    return render_template('index.html', tweets=results)

if __name__ == "__main__":
    app.run(debug=True)
