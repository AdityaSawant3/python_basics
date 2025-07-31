# Note: Superclas cannot access the methods of subclass.
class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1-A working.")

    def feature2(self):
        print("Feature 2 working.")

# Note: Subclass can access all the methods of superclass.
class B():

    # If no constructor specified it will call A's constructor.
    def __init__(self):
        super().__init__()
        # It always calls the Superclass's constructor after if we created B's instance unless we didn't specify.
        print("In B init")

    def feature1(self):
        print("Feature 1-B working.")

    def feature4(self):
        print("Feature 4 working.")

class C(A, B):

    def __init__(self):
        super().__init__()
        print("In C init")

# a1 = B()

a2 = C()
a2.feature1()

# It will call A's method because MRO (Method Resolution Order) is from left.
# C(A,B)