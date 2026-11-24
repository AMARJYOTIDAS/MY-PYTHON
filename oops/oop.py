class Car:
   brand ="dodge"
   
   def start(self):
     print("car is started")

car1 = Car()
print(car1.brand)

car1.start()
        #  car is a class
        #    brand is a variable
        #    and the start ans stop is method

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def start(self):
#         print(f"{self.brand} {self.model} is started.")

#     def stop(self):
#         print(f"{self.brand} {self.model} is stopped.")

class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(self.brand)


# Creating objects
car1 = Car("Dodge")
car2 = Car("Bugatti")

# Calling methods
car1.show()
car2.show()