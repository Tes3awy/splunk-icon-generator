from flask import Flask

from config import config


def create_app(config_name="production"):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Load config from the config.py object
    app.config.from_object(config.get(config_name, "default"))

    # Register Blueprints
    from app.core import bp as core_bp
    from app.error import bp as error_bp

    app.register_blueprint(core_bp, url_prefix="/")
    app.register_blueprint(error_bp)

    return app
