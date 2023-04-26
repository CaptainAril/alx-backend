#!/usr/bin/env python3
"""Set up for a basic Flask app."""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)


class Config:
    """config class for available languages in the app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


# @babel.localselector
def get_locale():
    """function that determines the best match with supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def hello():
    """renders templet `0-index.html`."""
    return render_template('3-index.html')


if __name__ == '(__main__)':
    app.run()
