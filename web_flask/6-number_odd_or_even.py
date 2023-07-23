#!/usr/bin/python3
"""
adding more routes
"""


from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def print_num(n):
    """
    printing text if n is an int
    """
    return ("{:d} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def print_num_temp(n):
    """
    rendering HTML template
    """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def print_num_odd_or_even(n):
    """
    render template only if int
    """
    if n % 2 == 0:
        state = "even"
    else:
        state = "odd"
    return render_template("6-number_odd_or_even.html", n=n, state=state)


if __name__ == "__main__":
    """
    run flask
    """
    app.run(host='0.0.0.0', port='5000')
