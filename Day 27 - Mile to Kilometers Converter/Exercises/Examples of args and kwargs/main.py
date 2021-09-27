def add(*args):  # unlimited and unspecified arguments
    print(args[0])  # type(args) = tuple
    sum = 0
    for n in args:
        sum += n

    return sum


sum_of_elements = add(8, 3, 2, 2, 2, 2, 2)
print(sum_of_elements)


def calculate(**kwargs):  # keywrod argument type(**kwargs) dict !
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])


calculate(add=3, multiply=3)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")  # if this key does not exits in the dict, return None. It wont give us error
        self.colour = kw("color")
        self.seats = kw("seats")


my_car = Car(make="Nissan")
print(my_car.model)
