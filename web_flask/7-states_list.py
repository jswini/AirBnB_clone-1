#!/usr/bin/python3
'''
This script opens a webflask application, loads from the storage,
and routes to a template
'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
# new_storage = storage


@app.teardown_appcontext
def teardown(context):
    '''
    This method closes the database
    '''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''
    renders the template in 7-states_list.html
    '''
    state = storage.all(State)
    return render_template('7-states_list.html', State=state)


if __name__ == "__main__":
    app.run(debug=True)
