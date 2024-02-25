import logging
import traceback

try:
    logger = logging.getLogger("logger")    #logger名loggerを取得
    logger.setLevel(logging.DEBUG)  #loggerとしてはDEBUGで

    #handler1を作成
    # handler1 = logging.StreamHandler()
    # handler1.setFormatter(logging.Formatter("%(asctime)s %(threadName)s %(levelname)8s %(message)s"))

    #handler2を作成
    handler2 = logging.FileHandler(filename="/proc/1/fd/1")  #handler2はdocker logが使うPID=1のstdoutファイルへ出力
    handler2.setFormatter(logging.Formatter("%(asctime)s %(threadName)s %(levelname)8s %(message)s"))

    #loggerに2つのハンドラを設定
    # logger.addHandler(handler1)
    logger.addHandler(handler2)

    #出力処理
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
except Exception as e:
    print(e)
    print(traceback.format_exc())
