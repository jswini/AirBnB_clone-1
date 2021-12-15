#!/usr/bin/python3
'''
this script creates a page to return hello hbnb
'''
from flask import Flask, render_template
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
    strict_slashes = False
    text = text.replace("_", " ")
    return 'C %s' % text


@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    '''this method prints the text from the var passed'''
    strict_slashes = False
    if "_" in text:
        text = text.replace("_", " ")
    return ('Python {}'.format(text))


@app.route('/number/<int:n>')
def number_text(n):
    '''this method displays a number'''
    strict_slashes = False
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>')
def number_html(n=None):
    '''this method displays a website from a template'''
    #strict_slashes = False
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    '''this method sets everything to work on 0.0.0.0'''
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
