import os
import sys
import json
import time
import random
from flask import g, request, make_response

sys.path.append(
    os.path.join(
        os.path.dirname(__file__), '../../common'
    )
)
from libs.MyLogger import Logger


def setup_ab_request_rest(app):
    """rest の before_requests/after_requests 定義用関数.
    """
    @app.before_request
    def before_request():
        """before_requests 定義.
        アクセスの情報出力及び,
        ログ用変数を設定
        """
        # 処理時間計測開始
        g.access_time = time.time()

        # ヘッダー取得
        headers = request.headers
        # ログのユニークキー初期化処理
        g.log_uniq_key = headers.get('LOG-UNIQ-KEY', '%08d' % random.randint(0, 99999999))
        # ログカウント数初期化処理
        g.log_count = headers.get('LOG-COUNT', 0)
        if isinstance(g.log_count, str) and str.isnumeric(g.log_count):
            g.log_count = int(g.log_count)
        else:
            g.log_count = 0

        # リクエストのエンドポイント/jsonを表示
        if request.method == 'GET':
            Logger.info(f'[REQUEST] GET: endpoint={request.url}, access={request.remote_addr}')
        elif request.method == 'POST':
            Logger.info(f'[REQUEST] POST: endpoint={request.url}, json={request.get_json()}')
        else:
            pass

    @app.after_request
    def after_request(response):
        """after_request 定義.
        アクセスにかかった時間等ログ出力,
        front へ log_uniq_key/log_count を返すためにヘッダー追加
        """
        # 処理にかかった時間を出力
        proc_time = (time.time() - g.access_time) * 1000
        Logger.info('time: {proc} ms   - done'.format(proc=round(proc_time, 3)))

        # レスポンスのログを可能であれば出しておく
        try:
            res = json.loads(response.get_data())
            Logger.info('[RESPONSE] {}'.format(res))
        except Exception:
            pass

        return response


def setup_ab_request_backend(app):
    """backend の before_requests/after_requests 定義用関数.
    """
    @app.before_request
    def before_request():
        """before_requests 定義.
        アクセスの情報出力及び,
        ログ用変数を設定
        """
        # 処理時間計測開始
        g.access_time = time.time()

        # ヘッダー取得
        headers = request.headers
        # ログのユニークキー初期化処理
        g.log_uniq_key = headers.get('LOG-UNIQ-KEY', '%08d' % random.randint(0, 99999999))
        # ログカウント数初期化処理
        g.log_count = headers.get('LOG-COUNT', 0)
        if isinstance(g.log_count, str) and str.isnumeric(g.log_count):
            g.log_count = int(g.log_count)
        else:
            g.log_count = 0

        # リクエストのエンドポイント/jsonを表示
        if request.method == 'GET':
            Logger.info(f'[REQUEST] GET: endpoint={request.url}, access={request.remote_addr}')
        elif request.method == 'POST':
            Logger.info(f'[REQUEST] POST: endpoint={request.url}, json={request.get_json()}')
        else:
            pass

    @app.after_request
    def after_request(response):
        """after_request 定義.
        アクセスにかかった時間等ログ出力,
        front へ log_uniq_key/log_count を返すためにヘッダー追加
        """
        # 処理にかかった時間を出力
        proc_time = (time.time() - g.access_time)
        Logger.info(f'time: {round(proc_time, 3)}   - done')

        # レスポンスのログを可能であれば出しておく
        try:
            res = json.loads(response.get_data())
            Logger.info(f'[RESPONSE] {res}')
        except Exception:
            pass

        # rest にログ用 log_uniq_key/log_count を返す
        res = make_response(response)
        res.headers['LOG-UNIQ-KEY'] = str(g.log_uniq_key)
        res.headers['LOG-COUNT'] = str(g.log_count)

        return res


def setup_ab_request_front(app):
    """rest の before_requests/after_requests 定義用関数.
    """
    @app.before_request
    def before_request():
        """before_requests 定義.
        アクセスの情報出力及び,
        ログ用変数を設定
        """
        # /static 配下へのアクセスは css/js 取得のためログは出さない
        if '/static' not in request.url:
            # 処理時間計測開始
            g.access_time = time.time()

            # ヘッダー取得
            headers = request.headers
            # ログのユニークキー初期化処理
            g.log_uniq_key = headers.get('LOG-UNIQ-KEY', '%08d' % random.randint(0, 99999999))
            # ログカウント数初期化処理
            g.log_count = headers.get('LOG-COUNT', 0)
            if isinstance(g.log_count, str) and str.isnumeric(g.log_count):
                g.log_count = int(g.log_count)
            else:
                g.log_count = 0

            # リクエストのエンドポイント/jsonを表示
            if request.method == 'GET':
                Logger.info(f'[REQUEST] GET: endpoint={request.url}, access={request.remote_addr}')
            elif request.method == 'POST':
                Logger.info(f'[REQUEST] POST: endpoint={request.url}, json={request.get_json()}')
            else:
                pass

    @app.after_request
    def after_request(response):
        """after_request 定義.
        アクセスにかかった時間等ログ出力,
        front へ log_uniq_key/log_count を返すためにヘッダー追加
        """
        # /static 配下へのアクセスは css/js 取得のためログは出さない
        if '/static' not in request.url:
            # 処理にかかった時間を出力
            proc_time = (time.time() - g.access_time) * 1000
            Logger.info('time: {proc} ms   - done'.format(proc=round(proc_time, 3)))

            # レスポンスのログを可能であれば出しておく
            try:
                res = json.loads(response.get_data())
                Logger.info('[RESPONSE] {}'.format(res))
            except Exception:
                pass

        return response
