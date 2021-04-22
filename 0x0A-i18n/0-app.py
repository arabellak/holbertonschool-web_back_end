#!/usr/bin/env python3
"""
    Flask app
"""
from app import app
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    return render_template('0-index')

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
