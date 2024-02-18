from libs.ErrorMessage import Error400, Error404


class MyException(Exception):
    """基本的なexception クラス

    Args:
        errorcode          : 6桁のエラーコード. httpstatus3桁, api内のエラーコード3桁の組み合わせ.
        message            : api内のエラーコード3桁から ErrorMessage から取得
        httpstatus         : httpstatus3桁
        custom_errorcode   : カスタムで利用するエラーコード. errorcode を利用しない場合利用.
        custom_errormessage: カスタムで利用するエラーメッセージ. errorcode を利用しない場合利用.
    """
    def __init__(self, errorcode=None, custom_errorcode=None, message=None, custom_errormessage=None):
        self.errorcode = str(errorcode) if errorcode is not None else None
        self.message = self.get_message()
        self.httpstatus = self.get_httpstatus()
        self.custom_errorcode = str(custom_errorcode)
        self.custom_errormessage = custom_errormessage

    def get_message(self):
        """errorcode よりメッセージ取得関数.
        Returns:
            message <str>: エラーメッセージを返却
        """
        if self.errorcode is not None:
            error_status, error_detail_code = self.errorcode[:3], self.errorcode[3:6]
            if error_status == "400":
                message = Error400.errormessage400[error_detail_code]
            elif error_status == "404":
                message = Error404.errormessage404[error_detail_code]
            else:
                message = "unknown error"
            return message

    def get_httpstatus(self):
        """httpstatus を取得する関数.

        Returns:
            errorcode <str>: 3桁のエラーコード
        """
        if self.errorcode is not None:
            return self.errorcode[:3]
        else:
            return None


class RESTAPIException(MyException):
    """RESTAPIException
    """
