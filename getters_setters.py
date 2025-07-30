class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter method
    def getName(self):
        return self.__name

    # Setter method
    def setAge(self, age):
        if age >= 18:
            self.__age = age
        else:
            print("Cannot get liscence.")

    def getAge(self):
        return self.__age

david = Person("David", 12)
print(f"My name is {david.getName()}, and my age is {david.getAge()}")

david.setAge(17)

jeff = Person("Jeff", 14)
print(f"My name is {jeff.getName()}, and my age is {jeff.getAge()}")
jeff.setAge(23)
print(f"My name is {jeff.getName()}, and my age is {jeff.getAge()}")

# Using decorators

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            print("Radius cannot be negative")

circle = Circle(5)
print(f"Initial radius: {circle.radius}")
circle.radius = 7
print(f"Updated radius: {circle.radius}")