##Login attempts

class User:

    def __init__ (self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.attempts = 0
        
    def describe_user(self):
        print(f"Best star wars character name is: {self.first_name}")

    def greet_user(self):
        print(f"{self.last_name} is the last name and is {self.age} years old.")

    def number_attempts(self, attempt):
        self.attempts = attempt
        return f"You have tried to log in {self.attempts} times."
    
    def increment_login_attempts(self, numbers):
        self.attempts += numbers

    def reset_login_attempts(self):
        self.attempts = 0

user1= User("grogu", "Din", 50)
user1.describe_user()
user1.greet_user()
user1.number_attempts(1)
user1.increment_login_attempts(1)

print(f"{user1.first_name.title()}'s age is {user1.age}")

print((user1.number_attempts(1)))

user1.reset_login_attempts()
print(f"You have tried to log in {user1.attempts} times.")


