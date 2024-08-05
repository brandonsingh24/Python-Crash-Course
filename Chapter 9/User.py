class User:

    def __init__ (self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}")

    def greet_user(self):
        print(f"{self.last_name} is the last name and is {self.age} years old.")