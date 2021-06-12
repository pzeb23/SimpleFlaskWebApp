from flask import Flask, render_template, redirect, request
# import requests
#import json
from newsapi import NewsApiClient
import random

app = Flask(__name__)


news_title = ""
news_content = ""
news_image = ""

@app.route("/") 
def home(): 
    return render_template('index.html', news_title=news_title, news_content = news_content, news_image = news_image)
    #return render_template('index.html') subfolder/page.html


@app.route("/getnewsparam", methods=["POST"])
def get_newsparam():

    seq = [0, 1, 2]
    api_key_index = random.choice(seq)

    news_api_keys = ['b251fd71f49b4976a8d549c9d51d9080', '40432cbc71b943658918e552616b21dd', 'c4a0b4bd8b0245ac96edf39ebb9a7ac5']

    newsapi = NewsApiClient(api_key=news_api_keys[api_key_index])

    query = request.form["query"]

    #top_headlines = newsapi.get_top_headlines(q=query, language='en')
    top_headlines = newsapi.get_everything(q=query, language='en')

    articles = top_headlines['articles']
    global news_title
    global news_content
    global news_image
    
    if top_headlines['totalResults'] == 0:
        news_title = "sorry, no content"
        news_content = "sorry, no content"
        news_image = "https://i.kym-cdn.com/entries/icons/original/000/019/277/confusedtravolta.jpg"

    else:
        news_title = articles[0]['title']
        news_content = articles[0]['content']
        news_image = articles[0]['urlToImage']

    return redirect(request.referrer)


#app.run(debug = True)
