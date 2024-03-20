"""python 基本的な使い方をしているAPI集

rest api 内で完結する.
"""

import os
import sys
import json
from flask import Blueprint

sys.path.append(
    os.path.join(
        os.path.dirname(__file__), '../../../common'
    )
)
from libs.Decorators import rest, front
from libs.MyException import RESTAPIException
from libs.MyLogger import Logger
from libs.WapperRenderTemplate import wapper_render_template


prefix_base = "/v1"
app = Blueprint("front_v1", __name__, url_prefix=prefix_base)


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


@app.route('/top', methods=['GET'])
@front.common()
def top_get():
    eventList = {
        'eventName': 'test',
        'startDate': 20240101,
        'endDate': 20240101,
        'userId': 1,
        'eventLink': 'test'
    }
    return wapper_render_template('top.html', eventList=eventList)


@app.route('/toperror', methods=['GET'])
@front.common()
def top_error():
    eventList = {
        'eventName': 'test',
        'startDate': 20240101,
        'endDate': 20240101,
        'userId': 1,
        'eventLink': 'test'
    }
    return wapper_render_template('top.html', eventLis=eventList)
