"""エラーコード管理用クラス群.
Error400: http statuscode が 400 の場合のエラー
Error404: http statuscode が 404 の場合のエラー
Error   : どうしようもないときに出すエラーの内容
"""


class Error400():
    errormessage400 = {
        '001': 'error message 400001'
    }


class Error404():
    errormessage404 = {
        '001': 'error message 404001'
    }


class Error():
    error = {
        'StatusCode': '400',
        'result': '',
        'ErrorMessaage': 'internal server_error'
    }
