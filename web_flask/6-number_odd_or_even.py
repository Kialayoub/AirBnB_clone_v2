#!/usr/bin/python3
"""Script to start a Flask web application"""
from flask import Flask, render_template

web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def greet_hbnb():
    """Display greeting message"""
    return "Hello HBNB!"


@web_app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display HBNB"""
    return "HBNB"


@web_app.route('/c/<string:text>', strict_slashes=False)
def display_c_text(text):
    """Display 'C' followed by the given text"""
    return "C %s" % text.replace('_', ' ')


@web_app.route("/python/", defaults={"text": "is cool"})
@web_app.route('/python/<string:text>', strict_slashes=False)
def display_python_text(text):
    """Display 'Python' followed by the given text"""
    return "Python %s" % text.replace('_', ' ')


@web_app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Display a message indicating that n is a number"""
    return "%d is a number" % n


@web_app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Display an HTML page"""
    return render_template("5-number.html", num=n)


@web_app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_odd_or_even(n):
    """Display an HTML page"""
    return render_template("6-number_odd_or_even.html", num=n)

if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)

