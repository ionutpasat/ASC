"""
Coffee Factory: A multiple producer - multiple consumer approach

Generate a base class Coffee which knows only the coffee name
Create the Espresso, Americano and Cappuccino classes which inherit the base class knowing that
each coffee type has a predetermined size.
Each of these classes have a get message method

Create 3 additional classes as following:
    * Distributor - A shared space where the producers puts coffees and the consumers takes them
    * CoffeeFactory - An infinite loop, which always sends coffees to the distributor
    * User - Another infinite loop, which always takes coffees from the distributor

The scope of this exercise is to correctly use threads, classes and synchronization objects.
The size of the coffee (ex. small, medium, large) is chosen randomly everytime.
The coffee type is chosen randomly everytime.

Example of output:

Consumer 65 consumed espresso
Factory 7 produced a nice small espresso
Consumer 87 consumed cappuccino
Factory 9 produced an italian medium cappuccino
Consumer 90 consumed americano
Consumer 84 consumed espresso
Factory 8 produced a strong medium americano
Consumer 135 consumed cappuccino
Consumer 94 consumed americano
"""
import threading
import random
import time

class Coffee:
    """ Base class """
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """ Returns the coffee name """
        return self.name

    def get_size(self):
        """ Returns the coffee size """
        raise NotImplementedError

class Espresso(Coffee):
    """ Espresso implementation """
    def __init__(self, size):
        super().__init__("espresso")
        self.size = size

    def get_message(self):
        """ Output message """
        return f"a nice {self.size} espresso"

class Americano(Coffee):
    """ Americano implementation """
    def __init__(self, size):
        super().__init__("americano")
        self.size = size

    def get_message(self):
        """ Output message """
        return f"a strong {self.size} americano"

class Cappuccino(Coffee):
    """ Cappuccino implementation """
    def __init__(self, size):
        super().__init__("cappuccino")
        self.size = size

    def get_message(self):
        """ Output message """
        return f"an italian {self.size} cappuccino"

class Distributor:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()
        self.producer_cv = threading.Condition(self.lock)
        self.consumer_cv = threading.Condition(self.lock)

    def add_coffee(self, coffee):
        with self.producer_cv:
            while len(self.queue) >= 1:
                self.producer_cv.wait()
            self.queue.append(coffee)
            self.consumer_cv.notify()

    def get_coffee(self):
        with self.consumer_cv:
            while len(self.queue) <= 0:
                self.consumer_cv.wait()
            self.producer_cv.notify()
            return self.queue.pop(0)

class CoffeeFactory:
    def __init__(self, distributor):
        self.distributor = distributor
        self.sizes = ["small", "medium", "large"]
        self.types = [Espresso, Americano, Cappuccino]

    def run(self):
        while True:
            coffee_type = random.choice(self.types)
            size = random.choice(self.sizes)
            coffee = coffee_type(size)
            print(f"Factory {threading.get_ident()} produced {coffee.get_message()} {coffee.get_name()}")
            self.distributor.add_coffee(coffee)
            time.sleep(2)

class User:
    def __init__(self, distributor, id):
        self.distributor = distributor
        self.id = id

    def run(self):
        while True:
            coffee = self.distributor.get_coffee()
            print(f"Consumer {self.id} consumed {coffee.get_name()}")
            time.sleep(2)

if __name__ == '__main__':
    distributor = Distributor()
    factory_threads = [threading.Thread(target=CoffeeFactory(distributor).run) for _ in range(3)]
    user_threads = [threading.Thread(target=User(distributor, i).run) for i in range(5)]

    for thread in factory_threads + user_threads:
        thread.start()

    for thread in factory_threads + user_threads:
        thread.join()