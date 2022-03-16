#!/usr/bin/python3
'''
This script will start a webflask app that starts a hello route page
'''
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_hbnb(strict_slashes=False):
    return 'Hello HBNB!'
