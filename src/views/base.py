from abc import ABC, abstractmethod
from models.base import BaseModel


class View[T: BaseModel](ABC):
    def __init__(self, data: list[T]) -> None:
        self._data = data

    def display(self):
        self._display_data()

    @abstractmethod
    def _display_data(self):
        raise NotImplementedError

    @property
    def data(self) -> list[T]:
        return self._data
