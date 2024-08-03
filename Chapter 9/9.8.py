##Admin

class Privileges:
    
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

Userprivileges = Privileges(['can add post', 'can delete post', 'can ban user'])


Userprivileges.show_privileges()

