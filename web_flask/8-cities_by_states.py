#!/usr/bin/python3
'''
This script opens a webflask application, loads from the storage,
and routes to a template
'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(context):
    '''
    This method closes the database
    '''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    '''
    render the template from cities by state
    '''
    state = storage.all(State)
    return render_template('8-cities_by_states.html', State=state)


if __name__ == "__main__":
    app.run(debug=True)
