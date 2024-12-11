class Singleton(type):
    _instances = None

    def __call__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__call__()
        return cls._instances


class A(metaclass=Singleton):
    pass

a = A()
b = A()
print(id(a), id(b))