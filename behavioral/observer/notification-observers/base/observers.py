from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from subjects import Subject


class Observer(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def notification(self, message: str) -> str:
        pass

    @abstractmethod
    def get_data(self, subject: Subject) -> str:
        pass

    def __str__(self):
        return "Observer({name})".format(name=self.name)
