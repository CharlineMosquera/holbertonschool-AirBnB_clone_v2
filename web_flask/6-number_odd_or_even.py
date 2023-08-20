#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """display “Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display “HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    """display text"""
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text='is cool'):
    """display text"""
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """display number"""
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_template(n):
    """display template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def show_odd_or_even(n):
    """display number odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
