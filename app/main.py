from flask import Flask, render_template, redirect, request
import requests
import json
from newsapi import NewsApiClient

app = Flask(__name__)

# Init
newsapi = NewsApiClient(api_key='b251fd71f49b4976a8d549c9d51d9080')
news_response = ""
news_content = ""
news_image = ""

@app.route("/")
def home_view():
	return "<h1>Welcome to Geeks for Geeks</h1>"

@app.route("/getnewsparam", methods=["POST"])
def get_newsparam():

    #query = request.form["query"]

    top_headlines = newsapi.get_top_headlines(q="microsoft", language='en')

    articles = top_headlines['articles']
    global news_response
    global news_content
    global news_image
    
    if top_headlines['totalResults'] == 0:
        news_response = "sorry, no content"
        news_content = "sorry, no content"
        news_image = "https://i.kym-cdn.com/entries/icons/original/000/019/277/confusedtravolta.jpg"

    else:
        news_response = articles[0]['title']
        news_content = articles[0]['content']
        news_image = articles[0]['urlToImage']

    #return redirect(request.referrer)
    return 2


#app.run(debug = True)
