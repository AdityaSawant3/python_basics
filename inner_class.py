# Outer class
class Student:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.id)
        self.lap.show()

    # Inner Class
    class Laptop():

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = '8'

        def show(self):
            print(self.brand, self.cpu, self.ram)

print("\nStudent details")
s1 = Student("Aditya", 23545)
s2 = Student("David", 55784)

s1.show()
s2.show()