class Vehicle:
    pass

print("Empty class name = ", Vehicle)

# Creating object of class.
car = Vehicle()
print(car)

class Vehicle:
    wheels = 4
    brand = "Rolles - Royce"
    doors = 4

car = Vehicle()
print(f"Car brand name is {car.brand} and it has {car.wheels} wheels and {car.doors} doors.")

# If we want to change any attribute from the Vehicle class we can do that with dot operator.
car.doors = 6
print(f"Car brand name is {car.brand} and it has {car.wheels} wheels and {car.doors} doors.")

van = Vehicle()
print(van.wheels)

Vehicle.wheels = 34
print(Vehicle.wheels)
print(car.wheels)

class Vehicle:
    wheels = 4

    def __init__(self, doors):
        print(f"Object created with doors = {doors}")

car = Vehicle(5)
van = Vehicle(6)

class Vehicle:

    def __init__(self, name):
        self.name = name

vehicle1 = Vehicle("Car")
vehicle2 = Vehicle("Van")

print(vehicle1.name)
print(vehicle2.name)

class Laptop:
    def __init__(self, brand, processor):
        self.brand = brand
        self.processor = processor

computer1 = Laptop("Acer", "Ryzen 7")
computer2 = Laptop("Mac", "M4")

print(computer1.brand, computer1.processor)
print(computer2.brand, computer2.processor)

class Vehicle:
    wheels = 4

car = Vehicle()
van = Vehicle()

print("Old Values")
print(car.wheels)
print(van.wheels)

car.wheels = 2

print("New Values")
print(car.wheels)
print(van.wheels)

print("Instance attributes of car", car.__dict__)
print("Instance attributes of van", van.__dict__)


class Laptop:
    __brand = "Acer" # Cannot access it.

    def write_code(self):
        print("Hello World")

pc = Laptop()
print("Method is called \n")
pc.write_code()

class Car:

    def __init__(self, brand, type):
        self.brand = brand
        self.type = type

    def accelerate(self, speed):
        print(f"{self.brand} travels with {speed} per hour")

car = Car("Rolles Royce", "Luxury")
car.accelerate(45)