#!/usr/bin/env python3
"""
    Babel setup
"""
from flask_babel import Babel
from flask import Flask, render_template
app = Flask(__name__)
babel = Babel(app)


class Config():
    """
        Configuration with languages and default location and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
        Determinates the best match with the supported langs
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_holberton():
    """Return
        - template 2-index
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
