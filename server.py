from flask import Flask
from flask import render_template
from api import getTweets
app = Flask(__name__)

@app.route("/")
def index():
    test = getTweets()
    return render_template('index.html', name=test)

if __name__ == "__main__":
    app.run(debug=True)
