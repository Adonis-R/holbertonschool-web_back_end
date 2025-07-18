#!/usr/bin/env python3
"""Flask app for i18n.

This module sets up a Flask application with Babel for internationalization.
It includes configuration for supported languages, default
locale, and timezone.
"""

from flask import Flask, render_template, request

from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Configuration class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


babel = Babel()


def get_locale():
    """Determine the best match for supported languages."""
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
    )


babel.init_app(app, locale_selector=get_locale)


@app.route('/', methods=['GET'])
def index():
    """Render the index.html template for the root route."""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
