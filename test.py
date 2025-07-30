class Square:

    def __init__(self, length):
        self.length = length

    def get_perimeter(self):
        return self.length * 4

    def get_area(self):
        return round(self.length * self.length)

square = Square(2)

# print(square.length)

# area = square.get_area()
# print(area)

# perimeter = square.get_perimeter()
# print(perimeter)

class Employee:

    retired_age = 50

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.salary = None
        self.remaining_years = None

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def years_to_work(self, present_age):
        self.remaining_years = self.retired_age - present_age
        return self.remaining_years

jeff = Employee("Jeff", 11020)
jeff.setSalary(34000)

# print(f"Salary: {jeff.getSalary()}")
# print(f"Years to work: {jeff.years_to_work(45)}")


class A:

    __dept = "Electronics"

    def department(self):
        print(f"{self.__dept} department")

class B(A):

    def department(self, dept):
        self.__dept = dept
        print(f"{self.__dept} department")

a = A()
a.department()

b = B()
b.department("Computer")


print("Hello ", __name__)