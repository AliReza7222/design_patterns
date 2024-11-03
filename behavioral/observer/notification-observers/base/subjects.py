from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from observers import Observer


class Subject(ABC):
    def __init__(self, initial_data: dict):
        self._observers = {}
        self._data = initial_data

    @abstractmethod
    def add_observer(self, observer: Observer, auto_updated: bool) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self, message: str) -> None:
        pass

    @abstractmethod
    def pull_data(self) -> dict:
        pass

    @abstractmethod
    def update(self, new_data: dict) -> None:
        pass
