## Restaurant

class Restaurant:

    def __init__ (self, name, diet):
        self.name = name
        self.diet = diet

    def describe_restaurant(self):
        print(f"The new restaurant's name is: {self.name}")
    def open_restaurant(self):
        print(f"{self.name} restaurant serves {self.diet}")

my_restaurant = Restaurant("Py's Bakery", "Pies")

print(f"My restaurant's name is {my_restaurant.name} that serves {my_restaurant.diet}")
my_restaurant.describe_restaurant()