class Car:

    # Class variable
    wheels = 4

    # Instance variable
    def __init__(self):
        self.mil = 10
        self.com = "Audi"

c1 = Car()
c2 = Car()

c1.mil = 9
print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)