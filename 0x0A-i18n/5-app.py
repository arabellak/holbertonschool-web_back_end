#!/usr/bin/env python3
"""
    Babel setup
"""
from flask_babel import Babel
from flask import Flask, render_template
from typing import Dict
app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user(login_as) -> Dict:
    """
        Return
         - User dictionary or None if ID cannot be found
    """
    if login_as in users:
        return users.get(login_as)
    return None

@app.before_request
def before_request():
    """
        Finds user and set it as global.
    """
    flask.g.user = get_user(user)


@app.route('/')
def hello_holberton():
    """Return
        - template 5-index
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
