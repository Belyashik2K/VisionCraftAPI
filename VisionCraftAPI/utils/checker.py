import re

from ..exceptions import *

class ExceptionChecker:
    def check(self, 
              exception: str,
              status_code: int = None):
        if "users can" in exception:
            self.prepaire_limit_message(exception)
        if "doesn't have" in exception or status_code == 422:
            self.prepaire_invalid_param(exception)
        if status_code == 403:
            raise InvalidAPIKey(message=exception)
        if status_code == 404:
            raise EndpointNotFound(message=exception,
                                   status_code=status_code)
        raise HTTPError(message=exception,
                        status_code=status_code)
    
    def prepaire_limit_message(self, 
                               exception: str):
        info = re.findall(r"(?<=per\s)\d+\s\w+", exception)
        retry_after, time_unit = info[0].split(" ")
        raise RateLimitExceeded(message=exception,
                                retry_after=retry_after,
                                time_unit=time_unit)
        
    def prepaire_invalid_param(self, 
                               exception: str | list):
        if isinstance(exception, list):
            exception = exception[0]['msg']
            param = "param"
        else:
            param = re.findall(r"(?<=doesn't have\s)\w+", exception)[0]
        raise InvalidParam(message=exception,
                           param=param)
        