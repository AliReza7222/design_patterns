from abc import ABC, abstractmethod


class BehaviorQuack(ABC):
    @abstractmethod
    def quack(self) -> str:
        pass

class BehaviorFly(ABC):
    @abstractmethod
    def fly(self) -> str:
        pass
