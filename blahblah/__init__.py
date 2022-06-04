from flask import Flask
from flask_restx import Api

from blahblah.config import Config
from blahblah.api import main_api

blahblah_api = Api(
    title="BlahBlah AI Api",
    version="1.0.0",
    doc=False,
)

def create_app(name: str = __name__):
    app: Flask = Flask(name)
    app.config.from_object(Config)

    blahblah_api.init_app(app)
    blahblah_api.add_namespace(main_api)

    return app