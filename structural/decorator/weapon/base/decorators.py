from typing import List

from weapons import Weapon


class WeaponsDecorator(Weapon):
    def __init__(self, weapon: Weapon):
        self._weapon = weapon

    @property
    def weapon(self) -> Weapon:
        return self._weapon

    def gun_parts(self) -> List[str]:
        return self._weapon.gun_parts()

    def cost(self) -> float:
        return self._weapon.cost()
