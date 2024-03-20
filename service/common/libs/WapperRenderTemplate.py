import traceback
from flask import render_template

from libs.MyLogger import Logger


def wapper_render_template(html, *a, **kw):
    """render_template 戻り値記録用 wapper 関数

    Args:
        html    : 利用 html 名
        *a      : 基本ない
        **kw    : jinja2 で利用する変数たち
    Returns:
        オリジナルの render_template で戻す
    """
    try:
        Logger.info(f'[RESPONSE] URL={html}, args={a}, kwargs={kw}')
    except Exception as e:
        Logger.error(e)
        Logger.error(traceback.format_exc())
    return render_template(html, *a, **kw)
