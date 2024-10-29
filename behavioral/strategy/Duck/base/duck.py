from typing import Optional

from .behaviors import *


class Duck:
    def __init__(self, name: str, behavior_fly: BehaviorFly,
        behavior_quack: BehaviorQuack):
        self.name = name
        self.behavior_fly: Optional[BehaviorFly] = behavior_fly
        self.behavior_quack: Optional[BehaviorQuack] = behavior_quack

    def set_behavior_fly(self, behavior_fly: BehaviorFly) -> None:
        self.behavior_fly = behavior_fly

    def set_behavior_quack(self, behavior_quack: BehaviorQuack) -> None:
        self.behavior_quack = behavior_quack

    def perform_behavior_fly(self) -> str:
        return self.behavior_fly.fly()

    def perform_behavior_quack(self) -> str:
        return self.behavior_quack.quack()

    def __str__(self) -> str:
        return f"{self.name} -> {self.perform_behavior_fly()} | {self.perform_behavior_quack()}"
