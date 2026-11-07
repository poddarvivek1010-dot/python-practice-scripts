#Basic OOP Classes and Object Instances


class ElectronicDevice:
    # setup that assigns simple fields to each device object
    def __init__(self, device_name, category_type):
        self.name = device_name
        self.category = category_type

    # simple function inside the class to show the item is running
    def turn_on(self):
        print(f"The {self.name} is booting up successfully!")

    #function that returns a formatted text fact about the item
    def check_category(self):
        return f"System Log: The {self.name} belongs to the {self.category} hardware group."

device_1 = ElectronicDevice("Laptop", "Computer")  # Instance 1

device_2 = ElectronicDevice("Smartphone", "Mobile")   # Instance 2


#Running the class functions to verify output
device_1.turn_on()
print(device_1.check_category())
print()  # for layout spacing
device_2.turn_on()
print(device_2.check_category())
