#!/usr/bin/env python3
"""GoHigherRecords.com - Permanent Static Site Server"""
from flask import Flask, send_file, redirect
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return send_file(os.path.join(BASE_DIR, 'index.html'))

@app.route('/index.html')
def index_html():
    return send_file(os.path.join(BASE_DIR, 'index.html'))

@app.route('/health')
def health():
    return {'status': 'ok', 'site': 'GoHigherRecords.com'}

@app.errorhandler(404)
def not_found(e):
    return send_file(os.path.join(BASE_DIR, 'index.html'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8090))
    app.run(host='0.0.0.0', port=port, debug=False)
