import os
import sys
import v1
import v2
import json
from config import config
from flask import Flask, jsonify

sys.path.append(
    os.path.join(
        os.path.dirname(__file__), '../../common'
    )
)
from libs.ABRequest import setup_ab_request_rest
from libs.MyLogger import Logger, setup_logger
from libs.Decorators import rest


app = Flask(__name__)
app.config.from_object(config)
app.config['SECRET_KEY'] = 'xNVg}f_m:UmiOB{9bC`SvB9j5N<-3I./'
app.config["JSON_AS_ASCII"] = False


setup_logger(dict_config=config.DICTCONFIG)
setup_ab_request_rest(app)
v1.setup(app)
v2.setup(app)


@app.route('/status', methods=["GET", "POST"])
@rest.common('000')
def hello_world():
    Logger.debug('TEST1')
    Logger.info('TEST2')
    Logger.warning('TEST3')
    Logger.error('TEST4')
    return jsonify({"message": "おーけー"})


@app.route('/status_jsonify', methods=["GET", "POST"])
@rest.common('001')
def hello_world_jsonify():
    return jsonify({"message": "おーけー"})


@app.route('/status_json', methods=["GET", "POST"])
@rest.common('002')
def hello_world_json():
    return json.dumps({"message": "おーけー"})


@app.route('/status_dict', methods=["GET", "POST"])
@rest.common('003')
def hello_world_dict():
    return {"message": "おーけー"}


# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')
