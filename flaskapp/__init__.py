import os

from datetime import datetime
from flask import Flask
from . import config

def create_app(env_name=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config.by_name[env_name or 'dev'])
    app.config.from_pyfile('config.py', silent=True)
    app.config.from_envvar('FLASKAPP_CONFIG_FILE', silent=True)

    @app.route('/')
    def index():
        return app.config['SAMPLE_MESSAGE']

    @app.route('/time')
    def current_time():
        return str(datetime.now())

    return app


