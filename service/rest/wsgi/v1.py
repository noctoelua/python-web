"""python 基本的な使い方をしているAPI集

rest api 内で完結する.
"""

import os
import sys
import json
from flask import Blueprint, jsonify

sys.path.append(
    os.path.join(
        os.path.dirname(__file__), '../../common'
    )
)
from libs.Decorators import rest
from libs.MyException import RESTAPIException
from libs.MyLogger import Logger


prefix_base = "/v1"
app = Blueprint("rest_v1", __name__, url_prefix=prefix_base)


def setup(root_app, url_prefix=""):
    root_app.register_blueprint(
        app, url_prefix="{prefix}{base}".format(prefix=url_prefix, base=prefix_base)
    )


@app.route('/status')
@rest.common('111')
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
@rest.common('112')
def get_test_recode():
    Logger.info('access test')
    return jsonify(
        {
            "message": "testおーけー"
        }
    )
