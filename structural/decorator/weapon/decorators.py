from typing import List

from base.decorators import WeaponsDecorator


class ButtstockDecorator(WeaponsDecorator):
    def gun_parts(self) -> List[str]:
        gun_parts = self._weapon.gun_parts()
        gun_parts.append("buttstock")
        return gun_parts

    def cost(self) -> float:
        return self._weapon.cost() + 15000


class OpticsDecorator(WeaponsDecorator):
    def gun_parts(self) -> List[str]:
        gun_parts = self._weapon.gun_parts()
        gun_parts.append("optics")
        return gun_parts

    def cost(self) -> float:
        return self._weapon.cost() + 17592.5


class MuzzleDeviceDecorator(WeaponsDecorator):
    def gun_parts(self) -> List[str]:
        gun_parts = self._weapon.gun_parts()
        gun_parts.append("muzzle")
        return gun_parts

    def cost(self) -> float:
        return self._weapon.cost() + 9999.99
