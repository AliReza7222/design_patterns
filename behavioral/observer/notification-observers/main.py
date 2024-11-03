from subjects import Data
from observers import *


def main():
    # define object observers
    player = ConcreteObserver(name="AliReza")
    student = ConcreteObserver(name="AliReza")
    butcher = ConcreteObserver(name="Asghar")

    data = Data(
        initial_data={
            "dollar": "650000$",
            "Euro": "750000$",
            "curent_currency": "Rial"
        }
    )

    data.add_observer(observer=player, auto_updated=True)
    data.add_observer(observer=student, auto_updated=False)
    data.add_observer(observer=butcher, auto_updated=True)

    data.update({"dollar": "900000$"})


    # pull data for student
    print(student.get_data(subject=data))


if __name__ == "__main__":
    main()
