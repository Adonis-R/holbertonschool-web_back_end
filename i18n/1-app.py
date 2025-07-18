#!/usr/bin/env python3
"""flask app for i18n
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Configuration class for Flask app.

    Defines available languages, default locale, and default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/', methods=['GET'])
def index():
    """Render the index.html template for the root route."""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
