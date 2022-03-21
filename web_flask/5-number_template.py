#!/usr/bin/python3
'''
This script will start a webflask app that starts a hello route page
'''
from flask import Flask, render_template
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
    return 'python {}'.format(new_text)


@app.route('/number/<int:n>')
def is_a_number(n, strict_slashes=False):
    '''
    This route checks if an input to a url with number is an int'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template_check(n, strict_slashes=False):
    '''
    This returns the HTML code for the template referenced.
    passing the variable n
    '''
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(debug=True)
