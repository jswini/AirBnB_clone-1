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


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''
    This is the route for Holberton bnb
    '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''
    This route creates a text response for statements about the c language
    '''
    new_text = text.replace('_', ' ')
    return 'c {}'.format(new_text)


@app.route('/python/<text>')
@app.route('/python')
@app.route('/python/')
def python_text(text='is cool', strict_slashes=False):
    '''
    This route creates a text response for statements about the python language
    '''
    new_text = text.replace('_', ' ')
    return 'Python {}'.format(new_text)


if __name__ == "__main__":
    app.run(debug=True)
