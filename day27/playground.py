""" *args AND **kwargs """


# args | unlimited arguments
def add(*args):
    sum_x = 0
    for arg in args:
        sum_x += arg
    return sum_x


# kwargs | keyword arguments
def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)


calculate(add=3, multiply=5)
print(add(3, 5, 6, 6, 6, 6, 6, 6))


class Car:

    def __init__(self, **kw):
        # use get() to print out none when there is no value for the param
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="BMW")
print(my_car.make)
