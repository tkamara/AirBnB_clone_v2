#!/usr/bin/python3
"""
writing a script that starts a flask app
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    printing at the home page
    """
    return("Hello HBNB!")


if __name__ == "__main__":
    """
    run flask
    """
    app.run(host='0.0.0.0', port='5000')
