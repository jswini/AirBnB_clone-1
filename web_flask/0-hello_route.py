#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
'''
this script creates a page to return hello hbnb
'''


@app.route('/')
def hello_HBNB():
    '''This method creates a route and gives it some text'''
    strict_slashes = False
    return 'Hello HBNB!'


if __name__ == '__main__':
    '''this method sets everything to work on 0.0.0.0'''
    app.debug = True
    app.run(host="0.0.0.0")
