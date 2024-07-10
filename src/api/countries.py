from aiohttp.client import ClientSession
from .base import API


class CountriesAPI(API):
    def __init__(self, session: ClientSession, url: str = r'https://restcountries.com/v3.1'):
        super().__init__(session, url)

    async def get_all(self) -> list:
        if json := await self._get('all/?fields=name,capital,flags'):
            return json if isinstance(json, list) else [json]
        return []
