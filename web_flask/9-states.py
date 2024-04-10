#!/usr/bin/python3
"""A script to initiate a Flask web application"""
from flask import Flask, render_template
from models import storage, State

my_app = Flask(__name__)


@my_app.teardown_appcontext
def close_db_session(exception):
    """Close the current SQLAlchemy Session after each request"""
    storage.close()


@my_app.route('/states', strict_slashes=False)
def display_states():
    """Display all states"""
    states = storage.all(State).values()
    return render_template("9-states.html", states=states, one=None)


@my_app.route('/states/<string:id>', strict_slashes=False)
def display_one_state(id):
    """Display one state if it exists"""
    k = "State." + id
    one = None
    if k in storage.all(State):
        one = storage.all(State)[k]
    return render_template("9-states.html", states=None, one=one)

if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)

