from flask import Flask ,render_template, redirect, request 
import requests
import json
from newsapi import NewsApiClient


app = Flask(__name__)

# Init
newsapi = NewsApiClient(api_key='b251fd71f49b4976a8d549c9d51d9080')

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='coronavirus',
#                                           language='en')
news_response = ""
news_content = ""
news_image = ""

@app.route("/") 
def home(): 
    return render_template('subfolder/page.html', news_response=news_response, news_content = news_content, news_image = news_image)

@app.route("/getposts", methods=["GET"])
def get_posts():
    r = requests.get('https://hacker-news.firebaseio.com/v0/askstories.json?print=pretty')
    jsonData = r.json()

    result = json.dumps(jsonData[:5])
    return result

@app.route("/getnews", methods=["GET"])
def get_news():
    result = top_headlines["articles"]

    return json.dumps(result)


@app.route("/getnewsparam", methods=["POST"])
def get_newsparam():

    query = request.form["query"]

    top_headlines = newsapi.get_top_headlines(q=query, language='en')

    articles = top_headlines['articles']
    global news_response
    global news_content
    global news_image
    
    if top_headlines['totalResults'] == 0:
        news_response = "sorry, no content"
        news_content = "sorry, no content"
        #news_image = "https://i.kym-cdn.com/entries/icons/original/000/019/277/confusedtravolta.jpg"

    else:
        news_response = articles[0]['title']
        news_content = articles[0]['content']
        news_image = articles[0]['urlToImage']

    return redirect(request.referrer)

app.run(debug = True)
