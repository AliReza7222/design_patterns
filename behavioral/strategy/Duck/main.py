from base.duck import Duck
from behaviors import *


def main():
    # Instances of Duck with different behaviors
    wooden_duck = Duck(
        name="wooden_duck",
        behavior_fly=NoFlight(),
        behavior_quack=SilentQuack()
    )
    nature_duck = Duck(
        name="nature_duck",
        behavior_fly=NaturalFly(),
        behavior_quack=NaturalQuack()
    )

    # Display behaviors
    print(wooden_duck)
    print(nature_duck)

    # Change behavior of wooden duck
    wooden_duck.set_behavior_fly(behavior_fly=NaturalFly())
    print(wooden_duck)


if __name__ == "__main__":
    main()
