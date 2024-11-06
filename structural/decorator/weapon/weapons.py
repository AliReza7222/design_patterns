from typing import List

from base.weapons import Weapon


class Akm(Weapon):
    def gun_parts(self) -> List[str]:
        return ["barrel", "receiver", "magazine"]

    def cost(self) -> float:
        return 100000
