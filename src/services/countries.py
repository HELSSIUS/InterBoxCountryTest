from api.countries import CountriesAPI
from models.countries import Country


class CountiesService:
    def __init__(self, countries_api: CountriesAPI) -> None:
        self.countries_api = countries_api

    async def get_all(self) -> list[Country]:
        json = await self.countries_api.get_all()
        countries = Country.from_json(json)
        return countries if isinstance(countries, list) else [countries]
