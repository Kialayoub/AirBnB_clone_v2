#!/usr/bin/python3
""" Flask web application script """
from flask import Flask

my_web_app = Flask(__name__)


@my_web_app.route('/', strict_slashes=False)
def greet_hbnb():
    """ Display greeting message """
    return "Hello HBNB!"


@my_web_app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Display HBNB """
    return "HBNB"


@my_web_app.route('/c/<string:text>', strict_slashes=False)
def display_c_text(text):
    """ Display 'C' followed by the given text """
    return "C %s" % text.replace('_', ' ')

if __name__ == '__main__':
    my_web_app.run(host='0.0.0.0', port=5000)

