import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        clone_obj = copy.deepcopy(self._objects.get(name))
        clone_obj.__dict__.update(kwargs)
        return clone_obj


def client_prototype(name, obj, **kwargs):
    prototype = Prototype()
    prototype.register(name, obj)
    return prototype.clone(name, **kwargs)


# example #

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('mahdi', 20)
p_clone = client_prototype('p', p, age=10)
print(p.__dict__)
print(p_clone.__dict__)
