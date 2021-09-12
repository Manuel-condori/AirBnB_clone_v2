#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, abort

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """ function to print """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ function to print """
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """ function to print """
    return "C {:s}".format(text).replace("_", " ")


@app.route("/python")
@app.route("/python/<text>")
def ptythont(text="is cool"):
    """ function to print """
    return "Python {:s}".format(text).replace("_", " ")


@app.route("/number/<n>")
def number(n):
    """ function to print """
    if n.isdigit() == True:
        return "{} is a number".format(n)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
