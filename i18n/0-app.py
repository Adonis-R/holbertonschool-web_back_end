#!/usr/bin/env python3
"""flask app for i18n
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Render the index.html template for the root route."""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
