class Laptop:

    fans = 2

    __hardware_no = "khkdhr34iui4yu4hr8"

    def __init__(self, brand, processor):
        self.brand = brand
        self.processor = processor

    def hardware(self):
        print(f"The hardware no is {self.__hardware_no}")


class Electronic(Laptop):

    def hardware(self):
        print("This is overriden method")
    
    def get_data(self):
        print("This is electronic device")

lp_1 = Laptop("Acer", "Ryzen 7")
lp_1.hardware()

# print(lp_1.brand)

device = Electronic("Acer", "R 7")
device.hardware()

device.get_data()

print(f"Is the Electoninc class the subclass of Laptop class: {issubclass(Electronic, Laptop)}")