import json
from flask import Blueprint, jsonify

from libs.Decorators import rest
from libs.MyException import RESTAPIException
from libs.MyLogger import Logger

from models import Test

prefix_base = "/bk"
app = Blueprint("web", __name__, url_prefix=prefix_base)


def setup(root_app, url_prefix=""):
    root_app.register_blueprint(
        app, url_prefix="{prefix}{base}".format(prefix=url_prefix, base=prefix_base)
    )


@app.route('/status')
@rest.common('011')
def hello_world_v1():
    return json.dumps(
        {
            "message": "v1おーけー"
        }
    )
