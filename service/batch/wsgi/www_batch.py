import os
import sys
from config import config
from flask import Flask, jsonify

sys.path.append(
    os.path.join(
        os.path.dirname(__file__), '../../common'
    )
)
from libs.MyLogger import Logger, setup_logger


app = Flask(__name__)
app.config.from_object(config)
app.config['SECRET_KEY'] = 'xNVg}f_m:UmiOB{9bC`SvB9j5N<-3I./'
app.config["JSON_AS_ASCII"] = False


setup_logger(dict_config=config.DICTCONFIG)


@app.route('/status', methods=["GET", "POST"])
def hello_world():
    Logger.info('batch status')
    return jsonify({"message": "おーけー"})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
