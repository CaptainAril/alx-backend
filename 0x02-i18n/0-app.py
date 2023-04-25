#!/usr/bin/env python3
"""Set up for a basic Flask app."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    """renders templet `0-index.html`."""
    return render_template('0-index.html')


if __name__ == '(__main__)':
    app.run()
