from base.subjects import Subject
from base.observers import Observer


class Data(Subject):
    def add_observer(self, observer: Observer, auto_updated: bool = True) -> None:
        if self._exsist_observer(observer):
            raise ValueError(
                "Observer {observer} is already added.".format(observer=observer)
            )
        self._observers[observer] = auto_updated

    def remove_observer(self, observer: Observer) -> None:
        if not self._exsist_observer(observer):
            raise ValueError(
                "Observer {observer} does not exist !".format(observer=observer)
            )
        del self._observers[observer]

    def _exsist_observer(self, observer: Observer):
        if self._observers.get(observer):
            return True
        return False

    def notify_observers(self, message: str) -> None:
        for observer, auto_update in self._observers.items():
            if auto_update:
                print(observer.notification(message=message))

    def pull_data(self) -> str:
        return self._data

    def update(self, new_data: dict) -> None:
        old_data = self._data.copy()
        self._data.update(new_data)
        msg = "data updated : {old_data} -> {new_data}".format(
            old_data=old_data, new_data=self._data
        )
        self.notify_observers(message=msg)
