#!/usr/bin/python3
"""
adding more routes
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    printing Hello HBNB!
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def print_HBNB():
    """
    printing HBNB
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def print_string(text):
    """
    printing the text
    """
    return ("C %s" % text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
def print_python(text):
    """
    printing the text
    """
    return ("Python %s" % text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
def print_py():
    """
    printing string
    """
    return ("Python is cool")


if __name__ == "__main__":
    """
    run flask
    """
    app.run(host='0.0.0.0', port='5000')
