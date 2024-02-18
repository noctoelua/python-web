import requests
from flask import g

from libs.MyLogger import Logger

class wapper_requests(object):
    """requests の wapper クラス.
    backend にアクセスする際に利用, LOG_UNIW_KEY/LOG_COUNT の受け渡しをする
    Args:
        object (_type_): _description_
    """
    def get(*a, **kw):
        # header に log_uniq_key / log_count を追加
        if "headers" in kw:
            headers = dict(**kw["headers"])
        else:
            headers = dict()
        headers["LOG_UNIQ_KEY"] = str(g.log_uniq_key)
        headers["LOG_COUNT"] = str(g.log_count + 1)
        kw["headers"] = headers

        # アクセス
        Logger.info(f"requests_args={kw}")
        res = requests.get(*a, **kw)
        # backend からの log_count を取得
        g.log_count = int(res.headers.get("LOG_COUNT", g.log_count))
        Logger.info(f"response status_code={res.status_code}, headers={res.headers}, res={res.json()}")

        return res.json()

class origin_requests(object):
    """requests のログ出力を補助する wapper クラス.
    ログのみのため requests と使い方は同じ.
    不要な場合は各ファイルで requests を使ってください.
    """
    def get(*a, **kw):
        # アクセス
        Logger.info(f"requests_args={kw}")
        res = requests.get(*a, **kw)
        Logger.info(f"response status_code={res.status_code}, headers={res.headers}, res={res.json()}")

        return res.json()
