#!/usr/bin/python3
"""Script to start a Flask web application"""
from flask import Flask, render_template
from models import storage, State

my_app = Flask(__name__)


@my_app.teardown_appcontext
def close_db_session(exception):
    """Close the current SQLAlchemy Session after each request"""
    storage.close()


@my_app.route('/cities_by_states', strict_slashes=False)
def display_state_cities():
    """Display all states and their cities"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)

if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)

