#!/usr/bin/python3
""" This module contains the code of the main Flask app """

from os import getenv
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_storage(exc):
    """Reload the storage"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """404 page not found"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    # set defaults if env variables are not set
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))

    # run the app
    app.run(host=host, port=port, threaded=True, debug=1)
