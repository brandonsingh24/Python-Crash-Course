### Number served

class Restaurant:

    def __init__ (self, name, diet):
        self.name = name
        self.diet = diet
        self.number_served = 1

    def describe_restaurant(self):
        return f"My restaurant serves {self.number_served} people."

    def update_number_served(self, number):
        self.number_served = number
        return self.describe_restaurant()
    
    def increment_served(self, numbers):
        self.number_served += numbers

my_restaurant = Restaurant('the','veggie')

#Default value
print(my_restaurant.number_served)

#Modifying value via method
my_new_restaurant = Restaurant('basic', 'meat')
my_new_restaurant.number_served = 4
print(my_new_restaurant.describe_restaurant())


## increment

my_new_restaurant.increment_served(299)
print(my_new_restaurant.describe_restaurant())