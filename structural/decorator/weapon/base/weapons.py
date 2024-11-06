from abc import ABC, abstractmethod
from typing import List



class Weapon(ABC):
    @abstractmethod
    def gun_parts(self) -> List[str]:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass
