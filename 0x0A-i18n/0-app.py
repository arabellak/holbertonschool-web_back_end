#!/usr/bin/env python3
"""
    Flask app
"""
from app import app


@app.route('/')
@app.route('0-index')

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
