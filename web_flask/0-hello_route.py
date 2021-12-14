#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_HBNB():
    strict_slashes=False
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
