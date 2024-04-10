#!/usr/bin/python3
"""A script to start a Flask web application"""
from flask import Flask, render_template
from models import storage, State, Amenity

my_app = Flask(__name__)


@my_app.teardown_appcontext
def close_db_session(exception):
    """Close the current SQLAlchemy Session after each request"""
    storage.close()


@my_app.route('/hbnb_filters', strict_slashes=False)
def display_states_amenities():
    """Display states and amenities"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", States=states, Amenities=amenities)


if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)
