from base.observers import Observer
from base.subjects import Subject


class ConcreteObserver(Observer):
    def notification(self, message: str):
        return "{observer}: {message}".format(observer=self, message=message)

    def get_data(self, subject: Subject):
        data = subject.pull_data()
        return "{observer}: Current data is {data}".format(observer=self, data=data)
