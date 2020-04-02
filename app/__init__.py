from flask import Flask
from app.persistence.db import mongo
import os

from .routes.v0 import cases
from .routes.v0 import contacts


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(cases)
    app.register_blueprint(contacts)

    env = os.environ.get("FLASK_ENV", "production")
    if env == "production":
        app.config.from_object("config.ProductionConfig")
    elif env == "development":
        app.config.from_object("config.DevelopmentConfig")
    elif env == "testing":
        app.config.from_object("config.TestingConfig")
        mongo_uri = os.environ.get("MONGO_URI")
        if mongo_uri is not None:
            app.config.update({"MONGO_URI": mongo_uri})

    mongo.init_app(app)
    return app
