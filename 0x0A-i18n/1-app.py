#!/usr/bin/env python3
"""
    Babel setup
"""
from flask import Flask
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('Config')
babel = Babel(app)


class Config():
    """
        Config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route('/')
def hello_holberton():
    """Return
        - template 0-index
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
