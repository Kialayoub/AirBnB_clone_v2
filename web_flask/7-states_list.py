#!/usr/bin/python3
"""Script to initiate a Flask web application"""
from flask import Flask, render_template
from models import storage, State

my_app = Flask(__name__)


@my_app.teardown_appcontext
def close_db_session(exception):
    """Close the current SQLAlchemy Session after each request"""
    storage.close()


@my_app.route('/states_list', strict_slashes=False)
def display_states():
    """Display all states"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)

if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)

