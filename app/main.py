from flask import Flask, render_template, redirect, request
import requests

app = Flask(__name__)

@app.route("/")
def home_view():
	return "<h1>Welcome to Geeks for Geeks</h1>"
