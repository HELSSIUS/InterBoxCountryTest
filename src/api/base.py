from abc import ABC, abstractmethod
from typing import Optional

from aiohttp import ClientSession


class API(ABC):
    def __init__(self, session: ClientSession, url: str) -> None:
        self.session = session
        self._url = url

    @abstractmethod
    async def get_all(self) -> Optional[dict | list]:
        raise NotImplementedError

    async def _get(self, relative_url: str) -> Optional[dict | list]:
        """ Get data from API endpoint by relative URL. """
        async with self.session.get(f"{self._url}/{relative_url}") as response:
            return await response.json()
