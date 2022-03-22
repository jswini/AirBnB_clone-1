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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    '''
    This route displays states, or cities with a state id
    '''
    state = storage.all(State)
    search_state = None
    if id:
        search_state = state.get("State." + id)
        state = None
    return render_template('/9-states.html', State=state,
                           search_state=search_state)


if __name__ == "__main__":
    app.run(debug=True)
