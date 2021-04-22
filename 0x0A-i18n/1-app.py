#!/usr/bin/env python3
"""
    Babel setup
"""
from flask import Flask
from flask_babel import Babel

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

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
