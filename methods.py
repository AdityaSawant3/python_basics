class School:

    school_name = "Electronics"

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def avg(self):
        return (self.m1 + self.m2) / 2

    # Class Method
    @classmethod
    def getSchool(cls):
        return cls.school_name

    # Static Method
    @staticmethod
    def info():
        print("This is Student Class") 

    
s1 = School(34, 56)
s2 = School(56, 23)

print(s1.avg())
print(s2.avg())

print(School.getSchool())

School.info()