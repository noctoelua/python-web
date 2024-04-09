import json
import time
import traceback
from flask import jsonify, render_template
from functools import wraps

from libs.MyLogger import Logger
from libs.MyException import RESTAPIException
from libs.ErrorMessage import Error


class rest():
    """API 用デコレータ.
    アクセス前処理はなし.
    アクセス後はレスポンスに
    * StatusCode を追加
    * Exception 処理
    """
    @classmethod
    def common(cls, api_pre_code):
        def deco(f):
            @wraps(f)
            def _wrapper(*args, **keywords):
                try:
                    ret = f(*args, **keywords)
                    # json 形式で帰ってきたら、一度dict化して StatusCode の追加
                    if type(ret) == str:
                        ret_json = json.loads(ret)
                        ret_json['StatusCode'] = '200'
                        return jsonify(ret_json)
                    # dict 形式で帰ってきたら StatusCode の追加
                    elif type(ret) == dict:
                        ret['StatusCode'] = '200'
                        return jsonify(ret)
                    # jsonify 形式 or その他形式の場合はそのまま
                    else:
                        return ret
                except RESTAPIException as e:
                    Logger.info('RESTAPIException に入りました')
                    if e.errorcode is not None:
                        ret_json = {
                            'StatusCode': e.httpstatus,
                            "ErrorCode": api_pre_code + e.errorcode,
                            "Message": e.message
                        }
                    else:
                        ret_json = {
                            'StatusCode': '404',
                            "ErrorCode": e.custom_errorcode,
                            "Message": e.custom_errormessage
                        }
                    return jsonify(ret_json)

                except Exception as e:
                    Logger.error(e)
                    Logger.error(traceback.format_exc())
                    return jsonify(Error.error)

            return _wrapper
        return deco


class front():
    """API 用デコレータ.
    アクセス前処理はなし.
    アクセス後はレスポンスに
    * StatusCode を追加
    * Exception 処理
    """
    @classmethod
    def common(cls):
        def deco(f):
            @wraps(f)
            def _wrapper(*args, **keywords):
                try:
                    ret = f(*args, **keywords)
                    return ret

                except Exception as e:
                    Logger.error(e)
                    Logger.error(traceback.format_exc())
                    error_message = [s.replace('\n', '') for s in str(traceback.format_exc()).split('\n')]
                    return render_template('err/error500.html', error_message=error_message)
            return _wrapper
        return deco


def db_log(log_flg=True, alert_limit=None):
    """db アクセス用ログ.
    経過時間及び, アクセスにかかった時間が想定以上の場合WARNINGレベルでエラーを出す.
    エラーが起こっても例外処理を行わないので各自頑張って.

    Args:
        log_flg <bool>    : ログ出力フラグ.
                            オフにするならそもそもデコレータ利用しなくてよい.
        alert_limit <float> : アクセスにかかった時間がこれ以上だとWARNINGレベルでログを出す.
    """
    def deco(f):
        @wraps(f)
        def _wrapper(*args, **keywords):
            start = time.time()
            if log_flg:
                Logger.info(f'[DB] access {f.__name__}')
            ret = f(*args, **keywords)
            proc_time = (time.time() - start)
            if log_flg:
                Logger.info(f'[DB] success {f.__name__}, time: {round(proc_time, 3)}  msec')
            if alert_limit:
                if alert_limit < proc_time:
                    Logger.warning(f'[DB] {f.__name__} is over alert_limit, time: {proc_time} msec')
            return ret
        return _wrapper
    return deco
