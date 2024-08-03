##Admin

class User:

    def __init__ (self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"Best star wars character name is: {self.first_name}")
    def greet_user(self):
        print(f"{self.last_name} is the last name and is {self.age} years old.")

user1= User("grogu", "Din", 50)
user1.describe_user()
user1.greet_user()

user2= User("djarin", "Din", 30)
user2.describe_user()
user2.greet_user()

print(f"{user1.first_name.title()}'s age is {user1.age} and {user2.first_name.title()}'s is {user2.age}")

class Privileges:
    
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
       self.privileges.show_privileges()

admin1 = Admin("Luke", "Skywalker", 53, ['can add post', 'can delete post', 'can ban user'])
admin1.show_privileges()

print(user1, admin1)
