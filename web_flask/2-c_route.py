#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """ function to print """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ function to print """
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """ function to print """
    a = text.replace('_', ' ')
    return 'C {}'.format(a)

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
