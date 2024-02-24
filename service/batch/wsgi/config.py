"""batch コンテナステータスチェック用.
API 利用がないためここの config はどうでもいい.
"""
import os


def get_config():
    """config を環境ごとに取得する関数.

    Returns:
        <class>
    """
    host_env = os.environ.get('POSITION', 'LOCAL')
    if host_env == 'LOCAL':
        return LocalConfig
    if host_env == 'DEV':
        return DevelopConfig
    else:
        return LocalConfig


class BaseConfig(object):
    """ベースとなる設定.
    各環境のクラスで継承して利用する.

    DICTCINFIG: Logger で利用する設定一覧のdict.
    DB_URI    : SQLAlchemy で利用する URI.
    """
    DICTCONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "root": {
            "level": "DEBUG",
            "handlers": [
                "consoleHandler",
                "logFileHandler"
            ]
        },
        "handlers": {
            "consoleHandler": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "consoleFormatter",
                "stream": "ext://sys.stdout"
            },
            "logFileHandler": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "level": "DEBUG",
                "formatter": "logFileFormatter",
                "filename": "/var/log/shizai_limeb_log.log",
                "encoding": "utf-8"
            }
        },
        "formatters": {
            "consoleFormatter": {
                "format": "%(asctime)s [%(levelname)-s] [%(log_uniq_key)s:%(log_count)s] %(message)s, %(txt)s [%(call_fullpath)s %(call_lineno)s in %(call_module)s]"
            },
            "logFileFormatter": {
                "format": "{asctime} [{levelname:^8s}] [{log_uniq_key}:{log_count}] {message}, {txt} [{call_fullpath} {call_lineno} in {call_module}]",
                "style": "{"
            }
        }
    }


class LocalConfig(BaseConfig):
    """local 用のcinfig

    log の level を DEBUG にすると,ユーザー設定した format で利用されている変数の利用ができなくてエラーがたくさん出るため注意.
    """
    DICTCONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "root": {
            "level": "INFO",
            "handlers": [
                "logFileHandler"
            ]
        },
        "handlers": {
            "logFileHandler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "logFileFormatter",
                "filename": "/var/log/shizai/web_log.log",
                "encoding": "utf-8",
                "maxBytes": 10000000,
                "backupCount": 3
            }
        },
        "formatters": {
            "logFileFormatter": {
                "format": "%(asctime)s [%(levelname)-7s] [%(log_uniq_key)s:%(log_count)s] %(message)s [%(call_fullpath)s %(call_lineno)s in %(call_module)s]"
            }
        }
    }


class DevelopConfig(BaseConfig):
    """DEV 用のcinfig
    """
    DICTCONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "root": {
            "level": "INFO",
            "handlers": [
                "consoleHandler"
            ]
        },
        "handlers": {
            "consoleHandler": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "consoleFormatter",
                "stream": "ext://sys.stdout"
            }
        },
        "formatters": {
            "consoleFormatter": {
                "format": "%(asctime)s [%(levelname)-7s] [%(log_uniq_key)s:%(log_count)s] %(message)s [%(call_fullpath)s %(call_lineno)s in %(call_module)s]"
            }
        }
    }


config = get_config()
