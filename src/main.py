import asyncio

from aiohttp.client import ClientSession
from rich.table import Table

from api.countries import CountriesAPI
from services.countries import CountiesService
from views.countries import CountriesView


async def main() -> None:
    async with ClientSession() as session:
        service = CountiesService(CountriesAPI(session))
        countries = await service.get_all()
        CountriesView(countries).display()


if __name__ == '__main__':
    asyncio.run(main())
