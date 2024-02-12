import requests
from flask import g

from libs.MyLogger import Logger

class wapper_requests(object):
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
    def get(*a, **kw):
        # アクセス
        Logger.info(f"requests_args={kw}")
        res = requests.get(*a, **kw)
        Logger.info(f"response status_code={res.status_code}, headers={res.headers}, res={res.json()}")

        return res.json()
