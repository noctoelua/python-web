import inspect
from logging import getLogger, config

from batch_config import config as batchconfig


def _get_logargs(batch_name, *args, **keywords):
    """ ユーザー定義のログ変数操作用関数
    batch_name   : 利用したバッチ名を記録するためのバッチ名.
    call_filename: Logger 呼びだしファイルの相対パス
    call_fullpath: Logger 呼びだしファイルの絶対パス
    call_module  : Logger 呼びだし関数名
    call_lineno  : Logger 呼びだし行数
    """
    _keys = dict()
    # バッチ名定義
    _keys['batch_name'] = batch_name

    # _get_loggers → Logger.info と親をたどり実際の呼び出し元ファイルを特定
    stack = inspect.currentframe().f_back.f_back
    _keys['call_filename'] = stack.f_code.co_filename
    _keys['call_fullpath'] = inspect.getabsfile(stack)
    _keys['call_module'] = stack.f_code.co_name
    _keys['call_lineno'] = stack.f_lineno

    # ユーザー定義用 log 変数定義
    keys = dict()
    keys['extra'] = _keys
    return args, keys


class Logger():
    """ 各種 logger へのログ出力.
    _get_logargs より必要パラメータ取得後ログ出力.
    """
    def __init__(self, batch_name='not defined'):
        """バッチで利用する logger 取得.

        Args:
            target <str>     : getLogger で利用する文字列. 得に決まりはない.
            batch_name <str> : バッチ名を渡してください.
        """
        config.dictConfig(batchconfig.DICTCONFIG)
        self.logger = getLogger(batch_name)
        self.batch_name = batch_name

    def debug(self, *args, **keywords):
        a, k = _get_logargs(self.batch_name, *args, **keywords)
        self.logger.debug(*a, **k)

    def info(self, *args, **keywords):
        a, k = _get_logargs(self.batch_name, *args, **keywords)
        self.logger.info(*a, **k)

    def warning(self, *args, **keywords):
        a, k = _get_logargs(self.batch_name, *args, **keywords)
        self.logger.warning(*a, **k)

    def error(self, *args, **keywords):
        a, k = _get_logargs(self.batch_name, *args, **keywords)
        self.logger.error(*a, **k)

    def critical(self, *args, **keywords):
        a, k = _get_logargs(self.batch_name, *args, **keywords)
        self.logger.critical(*a, **k)
