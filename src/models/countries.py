from dataclasses import dataclass
from typing import Union, Any, Literal, Self

from .base import BaseModel, Placeholder


@dataclass(frozen=True)
class Country(BaseModel):
    name: str | Literal[Placeholder.UNKNOWN]
    capital: str | Literal[Placeholder.UNKNOWN]
    flag_url: str | Literal[Placeholder.UNKNOWN]

    @classmethod
    def from_json(cls, data: dict[str, Any] | list[dict[str, Any]]) -> Union[Self, list[Self]]:
        if isinstance(data, list):
            return [cls._one_from_json(country) for country in data]

        if isinstance(data, dict):
            return cls._one_from_json(data)
        raise ValueError(f"Invalid data type: {type(data)} expected dict or list")

    @classmethod
    def _one_from_json(cls, data: dict[str, Any]) -> Self:
        name = data.get("name", {}).get("official", Placeholder.UNKNOWN.value)
        capital = data.get("capital", [])[0] if data.get("capital") else Placeholder.UNKNOWN.value
        flag_url = data.get("flags", {}).get("png", Placeholder.UNKNOWN.value)

        if not (name and capital and flag_url):
            raise ValueError(f"Invalid data: {data}")

        return cls(name, capital, flag_url)
