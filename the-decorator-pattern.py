import abc
# The decorator pattern provides a way to wrap methods or classes into other methods or classes.
# The decorators have to have the same type as the components they decorate.
# You can extend behaviour easily without subclassing.
# May result in multiple small classes.


class AbstractBeverage(metaclass=abc.ABCMeta):
    description: str = "Unknown"

    def getDescription(self) -> str:
        return self.description

    @abc.abstractmethod
    def cost(self) -> float:
        pass


class AbstractCondiment(AbstractBeverage, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getDescription(self) -> str:
        pass


class Espresso(AbstractBeverage):

    def __init__(self):
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99


class Latte(AbstractBeverage):

    def __init__(self):
        self.description = "Latte"

    def cost(self) -> float:
        return 2.99


class Mocha(AbstractCondiment):

    def __init__(self, beverage: AbstractBeverage):
        self.beverage = beverage

    def getDescription(self) -> str:
        return self.beverage.getDescription() + ', Mocha'

    def cost(self) -> float:
        return 0.2 + self.beverage.cost()


class Whip(AbstractCondiment):

    def __init__(self, beverage: AbstractBeverage):
        self.beverage = beverage

    def getDescription(self) -> str:
        return self.beverage.getDescription() + ', Whip'

    def cost(self) -> float:
        return 0.5 + self.beverage.cost()


beverage: AbstractBeverage = Espresso()
print("Simple espresso, no condiments is {}, description is {}".format(beverage.cost(), beverage.getDescription()))

beverage2: AbstractBeverage = Espresso()
beverage2 = Mocha(beverage2)
beverage2 = Whip(beverage2)
print("{} costs {}".format(beverage2.getDescription(), beverage2.cost()))

beverage3: AbstractBeverage = Latte()
beverage3 = Whip(beverage3)
print("{} costs {}".format(beverage3.getDescription(), beverage3.cost()))


