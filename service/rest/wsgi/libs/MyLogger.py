from logging.config import dictConfig
from flask import g, current_app
import inspect


def _get_logargs(*args, **keywords):
    """ ユーザー定義のログ変数操作用関数
    log_uniq_key : 1つのアクセスに1つのユニークキーを発行
    log_count    : アクセスに対するログ数をカウント
    call_filename: Logger 呼びだしファイルの相対パス
    call_fullpath: Logger 呼びだしファイルの絶対パス
    call_module  : Logger 呼びだし関数名
    call_lineno  : Logger 呼びだし行数
    """
    _keys = dict()
    # log 調査用ユニークキー設定
    _keys['log_uniq_key'] = g.log_uniq_key
    if not hasattr(g, "log_count"):
        g.log_count = 0
    g.log_count += 1
    _keys['log_count'] = g.log_count

    # _get_loggers → Logger.info と親をたどり実際の呼び出し元ファイルを特定
    stack = inspect.currentframe().f_back.f_back
    _keys['call_filename'] = stack.f_code.co_filename
    _keys['call_fullpath'] = inspect.getabsfile(stack)
    _keys['call_module'] = stack.f_code.co_name
    _keys['call_lineno'] = stack.f_lineno

    # デバック用テキスト出力変数
    _keys['txt'] = "test"

    # ユーザー定義用 log 変数定義
    keys = dict()
    keys['extra'] = _keys
    return args, keys


def setup_logger(dict_config=None):
    """ Logger フォーマット等設定関数
    dictConfig を利用して Config.py より設定.
    """
    # app.logger = getLogger(target)
    # for handler in app.logger.handlers:
    #     handler.setFormatter(config.LOG_FORMAT)
    #     handler.setLevel(loglevel)
    # if not app.logger.hasHandlers():
    #     file_handler = RotatingFileHandler(
    #         filename,
    #         maxBytes=10000000,
    #         backupCount=10,
    #         encoding='utf-8'
    #     )
    #     file_handler.setFormatter(Formatter(
    #         config.LOG_FORMAT)
    #     )
    #     app.logger.addHandler(file_handler)
    dictConfig(dict_config)


class Logger():
    """ 各種 logger へのログ出力
    _get_logargs より必要パラメータ取得後ログ出力.
    """
    def debug(*args, **keywords):
        a, k = _get_logargs(*args, **keywords)
        current_app.logger.debug(*a, **k)

    def info(*args, **keywords):
        a, k = _get_logargs(*args, **keywords)
        current_app.logger.info(*a, **k)

    def warning(*args, **keywords):
        a, k = _get_logargs(*args, **keywords)
        current_app.logger.warning(*a, **k)

    def error(*args, **keywords):
        a, k = _get_logargs(*args, **keywords)
        current_app.logger.error(*a, **k)

    def critical(*args, **keywords):
        a, k = _get_logargs(*args, **keywords)
        current_app.logger.critical(*a, **k)
