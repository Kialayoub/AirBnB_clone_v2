#!/usr/bin/python3
""" Script to initiate a Flask web application """
from flask import Flask

web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def greet_hbnb():
    """ Displays a greeting message """
    return "Hello HBNB!"


@web_app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Displays HBNB """
    return "HBNB"

if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)

