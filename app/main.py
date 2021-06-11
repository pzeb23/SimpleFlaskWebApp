from flask import Flask, render_template, redirect, request
#import requests
import json
from newsapi.newsapi_client import NewsApiClient

app = Flask(__name__)

# Init
newsapi = NewsApiClient(api_key='b251fd71f49b4976a8d549c9d51d9080')

@app.route("/")
def home_view():
	return "<h1>Welcome to Geeks for Geeks</h1>"
