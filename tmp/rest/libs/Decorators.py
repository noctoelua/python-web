import json
import traceback
from flask import jsonify
from functools import wraps

from libs.MyLogger import Logger
from libs.MyException import RESTAPIException
from libs.ErrorMessage import Error


class rest():
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
