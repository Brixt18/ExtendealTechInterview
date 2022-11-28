import logging

from flask import Flask

from .config.configuration import Development

app = Flask(__name__)


def configure_logging():
	FORMAT = """[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)s]    %(message)s\n"""
	logging.basicConfig(format=FORMAT)
	logging.disable(logging.INFO)


def create_app():
	app.config.from_object(Development)

	from .api import api_bp
	app.register_blueprint(api_bp)

	configure_logging()

	return app
