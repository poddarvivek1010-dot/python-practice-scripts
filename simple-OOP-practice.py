# Car Class Project


class CarRecord:
    #  storing simple information about cars
    def __init__(self, car_brand, car_color):
        self.brand = car_brand
        self.color = car_color

    # function to print out the details
    def display_car(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Color: {self.color}")


# Creating unique objects

#details of the first car
car_1 = CarRecord("Toyota", "Jet Black")

#details of the second car
car_2 = CarRecord("BMW", "dark Blue")

# details of the third car
car_3 = CarRecord("Mercedes-(G-Wagon)", "White")

# Running the class functions
print("Displaying Showroom Cars....")
car_1.display_car()

print()  # for layout spacing

car_2.display_car()

print()

cae_3.display_car()


