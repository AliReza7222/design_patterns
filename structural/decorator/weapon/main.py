from decorators import *
from weapons import *


def info_gun(weapon):
    return (
        "gun akm -> cost: {cost} and parts: {parts}\n".format(
            cost=akm_weapon.cost(),
            parts=akm_weapon.gun_parts()
        )
    )

if __name__ == "__main__":
    akm_weapon = Akm()
    print(info_gun(akm_weapon))

    akm_weapon = ButtstockDecorator(akm_weapon)
    print("Added feature to your gun.")
    print(info_gun(akm_weapon))

    akm_weapon = OpticsDecorator(MuzzleDeviceDecorator(akm_weapon))
    print("Added feature to your gun.")
    print(info_gun(akm_weapon))
