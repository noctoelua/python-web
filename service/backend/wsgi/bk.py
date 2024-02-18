# ライブラリ
import os
import sys
import json
from flask import Blueprint, jsonify
# 自前
sys.path.append(
    os.path.join(
        os.path.dirname(__file__), '../../common'
    )
)
from libs.Decorators import rest
from libs.MyException import RESTAPIException
from libs.MyLogger import Logger
from models.Shizai1 import Shizai1

prefix_base = "/bk"
app = Blueprint("web", __name__, url_prefix=prefix_base)


def setup(root_app, url_prefix=""):
    root_app.register_blueprint(
        app, url_prefix="{prefix}{base}".format(prefix=url_prefix, base=prefix_base)
    )


@app.route('/status')
@rest.common('011')
def hello_world_v1():
    ret_dict = Shizai1.get_shizai1_all()
    return json.dumps(ret_dict)
