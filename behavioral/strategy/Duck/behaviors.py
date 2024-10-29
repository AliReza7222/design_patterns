from base.behaviors import *


class SilentQuack(BehaviorQuack):
    def quack(self) -> str:
        return "Can't Quack!"

class NoFlight(BehaviorFly):
    def fly(self) -> str:
        return "Can't Fly!"

class NaturalQuack(BehaviorQuack):
    def quack(self) -> str:
        return "Quack!"

class NaturalFly(BehaviorFly):
    def fly(self) -> str:
        return "Flying!"
