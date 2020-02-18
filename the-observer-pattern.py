import abc
from typing import List

# Observer pattern defines a one to many dependency between objects so that when one object changes state,
# all of its dependents are notified and updated automatically.


class AbstractObserver(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        """Params are state values that the Observer gets from the subject when at least one changes"""
        pass


class AbstractSubject(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def registerObserver(self, observer: AbstractObserver) -> None:
        pass

    @abc.abstractmethod
    def notifyObservers(self) -> None:
        """Notify all Observers that the state has changed"""
        pass

    @abc.abstractmethod
    def removeObserver(self, observer: AbstractObserver) -> None:
        pass


class AbstractDisplayElement(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def display(self) -> None:
        pass


class Subject(AbstractSubject):
    observers: List[AbstractObserver] = []
    temp: float
    humidity: float
    pressure: float

    def registerObserver(self, observer: AbstractObserver) -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def notifyObservers(self) -> None:
        for item in self.observers:
            item.update(self.temp, self.humidity, self.pressure)

    def removeObserver(self, observer: AbstractObserver) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temp: float, humidity: float, pressure: float) -> None:
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()


class CurrentObserver(AbstractObserver, AbstractDisplayElement):
    temp: float
    humidity: float
    pressure: float

    def __init__(self, subject: AbstractSubject):
        """We use the subject to register this object as an observer."""
        subject.registerObserver(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self) -> None:
        print("for A temp is {}, humidity is {}, pressure is {}".format(self.temp, self.humidity, self. pressure))


class AnotherObserver(AbstractObserver, AbstractDisplayElement):
    temp: float
    humidity: float
    pressure: float

    def __init__(self, subject: AbstractSubject):
        """We use the subject to register this object as an observer."""
        subject.registerObserver(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self) -> None:
        print("for B temp is {}, humidity is {}, pressure is {}".format(self.temp, self.humidity, self. pressure))


class Testit():

    def test(self):
        subject = Subject()
        CurrentObserver(subject)
        AnotherObserver(subject)
        subject.setMeasurements(3,4,5)
        subject.setMeasurements(6,7,8)


test = Testit()
test.test()