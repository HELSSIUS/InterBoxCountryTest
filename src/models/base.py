from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
from typing import Union, Self


class Placeholder(str, Enum):
    UNKNOWN = "Unknown"


@dataclass(frozen=True)
class BaseModel(ABC):
    @classmethod
    @abstractmethod
    def from_json(cls, data: dict | list) -> Union[Self, list[Self]]:
        raise NotImplementedError
