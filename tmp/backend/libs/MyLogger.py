from logging.config import dictConfig
from flask import g, current_app
import inspect


"""_summary_
清書
"""
# def _get_logargs(*args, **keywords):
#         """_summary_
#         ユーザー定義のログ変数操作用関数
#         log_uniq_key : 1つのアクセスに1つのユニークキーを発行
#         log_count    : アクセスに対するログ数をカウント
#         """
#         _keys = dict()
#         # log 調査用ユニークキー設定
#         _keys['log_uniq_key'] = g.log_uniq_key
#         if not hasattr(g, "log_count"):
#             g.log_count = 0
#         g.log_count += 1
#         _keys['log_count'] = g.log_count

#         # _get_loggers → Logger.info と親をたどり実際の呼び出し元ファイルを特定
#         stack = inspect.currentframe().f_back.f_back
#         _keys['call_filename'] = stack.f_code.co_filename
#         _keys['call_fullpath'] = inspect.getabsfile(stack)
#         _keys['call_module'] = stack.f_code.co_name
#         _keys['call_lineno'] = stack.f_lineno

#         keys = dict()
#         keys['extra'] = _keys
#         return args, keys


# def setup_logger(app, target=None, filename=None, loglevel=DEBUG, dict_config=None):
#     dictConfig(dict_config)


# class Logger():
#     def debug(*args, **keywords):
#         a, k = _get_logargs(*args, **keywords)
#         current_app.logger.debug(*a, **k)

#     def info(*args, **keywords):
#         a, k = _get_logargs(*args, **keywords)
#         current_app.logger.info(*a, **k)

#     def warning(*args, **keywords):
#         a, k = _get_logargs(*args, **keywords)
#         current_app.logger.warning(*a, **k)

#     def error(*args, **keywords):
#         a, k = _get_logargs(*args, **keywords)
#         current_app.logger.error(*a, **k)


"""_summary_
下書き
"""
# class LogUtil(object):
#     def __init__(self, target=None, filename=None):
#         self.logger = getLogger(target)
#         self.logger.setLevel(DEBUG)
#         if not self.logger.hasHandlers():
#             file_handler = RotatingFileHandler(
#                 filename,
#                 maxBytes=10000,
#                 backupCount=10,
#                 encoding='utf-8'
#             )
#             file_handler.setFormatter(Formatter(
#                 '%(asctime)s %(levelname)s: %(message)s')
#             )
#             self.logger.addHandler(file_handler)


def _get_logargs(*args, **keywords):
    """_summary_
    ユーザー定義のログ変数操作用関数
    log_uniq_key : 1つのアクセスに1つのユニークキーを発行
    log_count    : アクセスに対するログ数をカウント
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
    # def __init__(self, app, target=None, filename=None):
    #     app.logger = getLogger(target)
    #     app.logger.setLevel(DEBUG)
    #     if not app.logger.hasHandlers():
    #         file_handler = RotatingFileHandler(
    #             filename,
    #             maxBytes=10000,
    #             backupCount=10,
    #             encoding='utf-8'
    #         )
    #         file_handler.setFormatter(Formatter(
    #             config.LOG_FORMAT)
    #         )
    #         app.logger.addHandler(file_handler)
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

    # def critical(*args, **keywords):
    #     a, k = _get_logargs(*args, **keywords)
    #     current_app.logger.critical(*a, **k)
