from abc import ABC, abstractmethod


class Being(ABC):
    def add(self, child):
        pass

    def remove(self, child):
        pass

    def is_composite(self):
        return False

    @abstractmethod
    def execute(self):
        pass


class Animal(Being):
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f'Animal {self.name}')


class Human(Being):
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def is_composite(self):
        return True

    def execute(self):
        print("Human execute")
        for child in self.children:
            child.execute()

class Male(Human):
    def __init__(self,name):
        self.name = name

    def execute(self):
        print(f"\t Male {self.name}")


class Female(Human):
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"\t Female {self.name}")


def client_composite():
    f1 = Female('mary')
    f2 = Female('larry')
    m1 = Male('John')

    h1 = Human()
    h1.add(f1)
    h1.add(m1)
    h1.add(f2)
    h1.execute()

client_composite()
