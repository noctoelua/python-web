"""python 基本的な使い方をしているAPI集

rest api 内で完結する.
"""
import os
import sys
from flask import Blueprint, jsonify, current_app

sys.path.append(
    os.path.join(
        os.path.dirname(__file__), '../../common'
    )
)
from libs.Decorators import rest
from libs.WapperRequests import origin_requests, wapper_requests

prefix_base = "/v2"
app = Blueprint("rest_v2", __name__, url_prefix=prefix_base)


def setup(root_app, url_prefix=""):
    root_app.register_blueprint(
        app, url_prefix="{prefix}{base}".format(prefix=url_prefix, base=prefix_base)
    )


@app.route('/status')
@rest.common('201')
def hello_world_v1():
    return jsonify({"message": "v2 おーけー"})


@app.route('/call2')
@rest.common('202')
def call():
    url = current_app.config['BACKEND_URL'] + 'status'
    res = origin_requests.get(url=url)
    return res


@app.route('/call3')
@rest.common('203')
def call3():
    url = current_app.config['BACKEND_URL'] + 'bk/status'
    res = wapper_requests.get(url)
    return res
