#!/usr/bin/python3
"""
starting flask application with 2 routes
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    print text
    """
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def print_HBNB():
    """
    print text
    """
    return("HBNB")


if __name__ == "__main__":
    """
    run flask
    """
    app.run(host='0.0.0.0', port='5000')
