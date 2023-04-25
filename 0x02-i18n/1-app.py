#!/usr/bin/env python3
"""Set up for a basic Flask app."""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """config class for available languages in the app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello():
    """renders templet `0-index.html`."""
    return render_template('1-index.html')


if __name__ == '(__main__)':
    app.run()
