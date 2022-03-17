#!/usr/bin/python3
'''
This script will start a webflask app that starts a hello route page
'''
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    '''
    This is the basic route
    '''
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(debug=True)
