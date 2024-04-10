#!/usr/bin/python3
"""Script to start a Flask web application"""
from flask import Flask

my_app = Flask(__name__)


@my_app.route('/', strict_slashes=False)
def greet_hbnb():
    """Display greeting message"""
    return "Hello HBNB!"


@my_app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display HBNB"""
    return "HBNB"


@my_app.route('/c/<string:text>', strict_slashes=False)
def display_c_text(text):
    """Display 'C' followed by the given text"""
    return "C %s" % text.replace('_', ' ')


@my_app.route("/python/", defaults={"text": "is cool"})
@my_app.route('/python/<string:text>', strict_slashes=False)
def display_python_text(text):
    """Display 'Python' followed by the given text"""
    return "Python %s" % text.replace('_', ' ')

if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)

