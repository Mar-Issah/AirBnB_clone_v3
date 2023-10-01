#!/usr/bin/python3xx
"""Index file"""


from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def get_status():
    """am method that returns a JSON: status: OK"""
    return jsonify(status='OK')
