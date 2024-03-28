import ssl
import certifi

from typing import Optional
from aiohttp import ClientSession, TCPConnector

from .utils import checker

class HTTPClient:
    """Represents an HTTP client sending HTTP requests to the API."""

    def __init__(self) -> None:
        ...

    async def __aenter__(self, *args, **kwargs) -> None:
        """Create a new session."""
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        connector = TCPConnector(ssl=ssl_context)
        self._session = ClientSession(connector=connector)

    async def __aexit__(self, *args, **kwargs) -> None:
        """Close the session."""
        await self._session.close()

    async def _request(self, 
                       method: str,
                       url: str, 
                       **kwargs) -> Optional[dict]:
        """Make a request to the API."""
        async with self:
            async with self._session.request(method, url, **kwargs) as response:
                if response.content_type == 'application/json':
                    data = await response.json()
                elif response.content_type == 'text/plain':
                    data = await response.text()
                else:
                    data = await response.read()
            return self.__check_exception(data=data, 
                                          status_code=response.status)
            
    def __check_exception(self, 
                          data: str,
                          status_code: int):
        """Check if the response contains an exception."""
        if isinstance(data, dict):
            if data.get('error') or data.get('detail'):
                exception = data.get('error') or data.get('detail')
                checker.check(exception=exception,
                              status_code=status_code)
        if status_code != 200:
            checker.check(exception=data,
                          status_code=status_code)
        return data