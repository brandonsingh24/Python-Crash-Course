## Three Restaurants

class Restaurant:

    def __init__ (self, name, diet):
        self.name = name
        self.diet = diet

    def describe_restaurant(self):
        print(f"The new restaurant's name is: {self.name}")
    def open_restaurant(self):
        print(f"{self.name} restaurant serves {self.diet}")

my_restaurant = Restaurant("Py's Bakery", "Pies")
her_restaurant = Restaurant("Do-nut", "doughnuts")
your_restaurant = Restaurant("Apple Time", "oranges")

print(f"My restaurant's name is {my_restaurant.name} that serves {my_restaurant.diet}")
my_restaurant.describe_restaurant()

print(f"My restaurant's name is {her_restaurant.name} that serves {her_restaurant.diet}")
her_restaurant.describe_restaurant()

print(f"My restaurant's name is {your_restaurant.name} that serves {your_restaurant.diet}")
your_restaurant.describe_restaurant()