import json
import time
import random
from flask import g, request

from libs.MyLogger import Logger


def setup_ab_request_rest(app):
    @app.before_request
    def before_request():
        # 処理時間計測開始
        g.access_time = time.time()

        # ヘッダー取得
        headers = request.headers
        # ログのユニークキー初期化処理
        g.log_uniq_key = headers.get('LOG_UNIQ_KEY', '%08d' % random.randint(0, 99999999))
        # ログカウント数初期化処理
        g.log_count = headers.get('LOG_COUNT', 0)
        if isinstance(g.log_count, str) and str.isnumeric(g.log_count):
            g.log_count = int(g.log_count)
        else:
            g.log_count = 0

        # リクエストのエンドポイント/jsonを表示
        if request.method == 'GET':
            Logger.info('[REQUEST] GET: endpoint={}'.format(request.url))
        elif request.method == 'POST':
            Logger.info('[REQUEST] POST: endpoint={}, json={}'.format(request.url, request.get_json()))
        else:
            pass

    @app.after_request
    def after_request(response):
        # 処理にかかった時間を出力
        proc_time = (time.time() - g.access_time) * 1000
        Logger.info('time: {proc}   - done'.format(proc=round(proc_time, 3)))

        # レスポンスのログを可能であれば出しておく
        try:
            res = json.loads(response.get_data())
            Logger.info('[RESPONSE] {}'.format(res))
        except Exception:
            pass

        return response
