class InvalidAPIKey(Exception):
    """
    Raised when an invalid API key is provided.
    """
    def __init__(self, 
                 message: str) -> None:
        super().__init__()
        self.message = message
        
    def __str__(self) -> str:
        return f'VisionCraft API says: "{self.message}". Please provide a valid API key.'
    
class InvalidParam(Exception):
    """
    Raised when an invalid param is provided.
    """
    def __init__(self, 
                 message: str,
                 param: str) -> None:
        super().__init__()
        self.message = message
        self.param = param
        
    def __str__(self) -> str:
        return f'VisionCraft API says: "{self.message}". Please provide a valid {self.param}.'
    
class HTTPError(Exception):
    """
    Raised when an HTTP error occurs.
    """
    def __init__(self, 
                 message: str,
                 status_code: int) -> None:
        super().__init__()
        self.message = message
        self.status_code = status_code
        
    def __str__(self) -> str:
        return f'VisionCraft API says: "{self.message}". Status code: {self.status_code}.'

class EndpointNotFound(HTTPError):
    """
    Raised when an endpoint is not found.
    """
    def __init__(self, 
                 message: str,
                 status_code: int) -> None:
        super().__init__(message, status_code)
        
    def __str__(self) -> str:
        return f'VisionCraft API says: "{self.message}". Endpoint not found.'
       
class RateLimitExceeded(Exception):
    """
    Raised when the rate limit is exceeded.

    Check https://api.visioncraft.top/limits for more information.
    """
    def __init__(self, 
                 message: str,
                 retry_after: int,
                 time_unit: str) -> None:
        super().__init__()
        
        retry_after = int(retry_after)
        
        times = {
            'seconds': retry_after,
            'minutes': retry_after * 60,
            'hours': retry_after * 60 * 60,
        }
        
        self.message = message
        self.retry_after = times[time_unit.replace(".", "")]
        
    def __str__(self) -> str:
        return f'VisionCraft API says: "{self.message}". Retry after {self.retry_after} seconds.'