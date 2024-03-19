

class RequestStatus(object):
    
    def __init__(self, success: bool, error_msg: str) -> None:
        self._success = success
        self._error_msg = error_msg
        

    @property
    def success(self):
        return self._success

    @property
    def error_msg(self):
        return self._error_msg
   
    def print_error(self):
        print(self.error_msg)
    