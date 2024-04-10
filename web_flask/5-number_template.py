#!/usr/bin/python3
"""Script to initiate a Flask web application"""
from flask import Flask, render_template

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


@my_app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Display a message indicating that n is a number"""
    return "%d is a number" % n


@my_app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Display an HTML page"""
    return render_template("5-number.html", num=n)

if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)

