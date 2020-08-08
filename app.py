from flask import Flask, render_template, request
import praw, prawcore
from datetime import datetime

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     user_agent="")

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            redditor = reddit.redditor(request.form['username'])
            redditor.created_utc = datetime.fromtimestamp(redditor.created_utc)

            return(render_template("index.html", redditor=redditor))
        except prawcore.exceptions.NotFound:
            return(render_template("index.html", error="This redditor could not be found."))

    return render_template("index.html")