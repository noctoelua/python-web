from libs.ErrorMessage import Error400, Error404


class MyException(Exception):
    def __init__(self, errorcode=None, custom_errorcode=None, message=None, custom_errormessage=None):
        self.errorcode = str(errorcode) if errorcode is not None else None
        self.message = self.get_message()
        self.httpstatus = self.get_httpstatus()
        self.custom_errorcode = str(custom_errorcode)
        self.custom_errormessage = custom_errormessage

    def get_message(self):
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
        if self.errorcode is not None:
            return self.errorcode[:3]
        else:
            return None


class RESTAPIException(MyException):
    """RESTAPIException
    """
