import json
from flask import Blueprint, jsonify

from libs.Decorators import rest
from libs.MyException import RESTAPIException
from libs.MyLogger import Logger

from models import Test

prefix_base = "/v1"
app = Blueprint("web", __name__, url_prefix=prefix_base)


def setup(root_app, url_prefix=""):
    root_app.register_blueprint(
        app, url_prefix="{prefix}{base}".format(prefix=url_prefix, base=prefix_base)
    )


@app.route('/status')
@rest.common('011')
def hello_world_v1():
    Logger.info("access status")
    import random
    a = random.randint(0, 2)
    b = random.randint(0, 2)
    c = a / b
    if c == 1:
        return json.dumps(
            {
                "message": "v1おーけー"
            }
        )

    if c == 2:
        raise RESTAPIException(
            custom_errorcode=123456789,
            custom_errormessage="r-sakairi"
        )

    else:
        raise RESTAPIException(
            errorcode=400001
        )


@app.route('/test')
@rest.common('012')
def get_test_recode():
    Logger.info('access test')
    test = Test.get_top_user
    return jsonify(
        {
            "message": "testおーけー"
        }
    )
    # return test
