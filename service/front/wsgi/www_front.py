import os
import sys
from controllers import v1
# import v2
from config import config
from flask import Flask, jsonify

sys.path.append(
    os.path.join(
        os.path.dirname(__file__), '../../common'
    )
)
from libs.RestABRequest import setup_ab_request_front
from libs.MyLogger import Logger, setup_logger
from libs.Decorators import rest


app = Flask(__name__)
app.config.from_object(config)
app.config['SECRET_KEY'] = 'xNVg}f_m:UmiOB{9bC`SvB9j5N<-3I./'
app.config["JSON_AS_ASCII"] = False


setup_logger(dict_config=config.DICTCONFIG)
setup_ab_request_front(app)
v1.setup(app)
# v2.setup(app)


@app.route('/status', methods=["GET", "POST"])
@rest.common('000')
def hello_world():
    Logger.debug('TEST1')
    Logger.info('TEST2')
    Logger.warning('TEST3')
    Logger.error('TEST4')
    return jsonify({"message": "おーけー"})


if __name__ == '__main__':
    """デバック実行用.
    基本的には app_*.ini より起動する.
    """
    debug = True
    port = '7000'
    host = '0.0.0.0'

    app.run(debug=debug, port=port, host=host)
