import abc

# Using an abstract factory we decouple the code from the actual factory that creates the products. So we can have a
# variety of factories that produce products for different contexts.
# This is the abstract factory pattern that creates objects through compositions, rather than inheritance like the
# factory method. Abstract factories are useful when you have families of products. While Factory method is useful to
# decouple your client code from the concrete classes you need to instantiate.


class AbstractPizza(metaclass=abc.ABCMeta):
    name: str
    dough: str
    sauce: str

    @abc.abstractmethod
    def prepare(self):
        pass

    @abc.abstractmethod
    def deliver(self):
        pass

    def setName(self, name: str):
        self.name = name


class AbstractPizzaFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def createDough(self):
        pass

    @abc.abstractmethod
    def createSauce(self):
        pass

    @abc.abstractmethod
    def createCheese(self):
        pass

    @abc.abstractmethod
    def createVeggies(self):
        pass


class NYPizzaFactory(AbstractPizzaFactory):

    def createDough(self):
        return ThinCrustDough()

    def createCheese(self):
        return ReggianoCheese()

    def createSauce(self):
        return MarinaraSauce()

    def createVeggies(self):
        veggies = [Garlic(), Onion(), Mushroom()]
        return veggies


class ChicagoPizzaFactory(AbstractPizzaFactory):

    def createDough(self):
        return ThickCrustDough()

    def createCheese(self):
        return Mozzarella()

    def createSauce(self):
        return PlumTomatoSauce()

    def createVeggies(self):
        veggies = [Eggplant(), Spinach()]
        return veggies


class CheesePizza(AbstractPizza):

    def __init__(self, pizzaFactory: AbstractPizzaFactory):
        self.pizzaFactory = pizzaFactory

    def prepare(self) -> None:
        print("Preparing {}".format(self.name))
        dough = self.pizzaFactory.createDough()
        print("Type of dough is {}".format(dough.name))
        sauce = self.pizzaFactory.createSauce()
        print("Type of sauce is {}".format(sauce.name))
        cheese = self.pizzaFactory.createCheese()
        print("Type of topping is {}".format(cheese.name))

    def deliver(self):
        print("Delivering your {} pizza".format(self.name))


class VeganPizza(AbstractPizza):

    def __init__(self, pizzaFactory: AbstractPizzaFactory):
        self.pizzaFactory = pizzaFactory

    def prepare(self) -> None:
        print("Preparing {}".format(self.name))
        dough = self.pizzaFactory.createDough()
        print("Type of dough is {}".format(dough.name))
        sauce = self.pizzaFactory.createSauce()
        print("Type of sauce is {}".format(sauce.name))
        veggie = self.pizzaFactory.createVeggies()
        print("Type of topping is {}".format(", ".join(map(lambda x: x.name, veggie))))

    def deliver(self):
        print("Delivering your {}".format(self.name))


class AbstractPizzaStore(metaclass=abc.ABCMeta):

    def orderPizza(self, type: str) -> AbstractPizza:
        pizza: AbstractPizza = self.createPizza(type)
        pizza.prepare()
        pizza.deliver()

        return pizza

    @abc.abstractmethod
    def createPizza(self, item: str) -> AbstractPizza:
        pass


class NYPizzaStore(AbstractPizzaStore):

    def createPizza(self, item: str) -> AbstractPizza:
        pizza: AbstractPizza
        pizzaFactory = NYPizzaFactory()
        if item == "cheese":
            pizza = CheesePizza(pizzaFactory)
            pizza.setName("NY Cheese Pizza")
        elif item == "veggie":
            pizza = VeganPizza(pizzaFactory)
            pizza.setName("NY Vegan Pizza")
        else:
            raise Exception("Wrong type of pizza submitted")

        return pizza


class ChicagoPizzaStore(AbstractPizzaStore):

    def createPizza(self, item: str) -> AbstractPizza:
        pizza: AbstractPizza
        pizzaFactory = ChicagoPizzaFactory()
        if item == "cheese":
            pizza = CheesePizza(pizzaFactory)
            pizza.setName("Chicago Cheese Pizza")
        elif item == "veggie":
            pizza = VeganPizza(pizzaFactory)
            pizza.setName("Chicago Vegan Pizza")
        else:
            raise Exception("Wrong type of pizza submitted")

        return pizza


class AbstractDough(metaclass=abc.ABCMeta):
    name: str

class ThinCrustDough(AbstractDough):
    name = "Thin crust dough"

class ThickCrustDough(AbstractDough):
    name = "Thick crust dough"

class AbstractCheese(metaclass=abc.ABCMeta):
    name: str

class ReggianoCheese(AbstractCheese):
    name = "Reggiano cheese"

class Mozzarella(AbstractCheese):
    name = "Mozzarella cheese"

class AbstractSauce(metaclass=abc.ABCMeta):
    name: str

class MarinaraSauce(AbstractSauce):
    name = "Marinara sauce"

class PlumTomatoSauce(AbstractSauce):
    name = "Plum tomato sauce"

class AbstractVeggies(metaclass=abc.ABCMeta):
    name: str

class Garlic(AbstractVeggies):
    name = "Garlic toping"

class Onion(AbstractVeggies):
    name = "Onion toping"

class Mushroom(AbstractVeggies):
    name = "Mushroom toping"

class Eggplant(AbstractVeggies):
    name = "Eggplant toping"

class Spinach(AbstractVeggies):
    name = "Spinach toping"


nypizza = NYPizzaStore()
my_pizza = nypizza.orderPizza("cheese")

chicago_pizza = ChicagoPizzaStore()
my_chicago_pizza = chicago_pizza.orderPizza("veggie")
