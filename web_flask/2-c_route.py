#!/usr/bin/python3
'''
this script creates a page to return hello hbnb
'''
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_HBNB():
    '''This method creates a route and gives it some text'''
    strict_slashes = False
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    '''this method routes to /hbnb'''
    strict_slashes = False
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    '''this method prints the text from the var passed'''
    return 'C %s' % text


if __name__ == '__main__':
    '''this method sets everything to work on 0.0.0.0'''
    app.debug = True
    app.run(host="0.0.0.0")
