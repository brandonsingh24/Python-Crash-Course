##5.10

current_users = ['marge', 'maggie', 'bart', 'homer', 'lisa', 'admin']
#current_users2 = ['MARGE', 'MAGGIE', 'BART', 'HOMER', 'LISA', 'ADMIN']

#Probably better code here:
#current_users_lower = []
#for user in current_users:
#    current_users_lower.append(user.lower())
### OR
current_users = [user.lower() for user in current_users]

new_users = ['mr burns', 'smithers', "homer", 'lenny', 'carl']

for new_user in new_users:
#    if new_user in current_users and current_users2:
    if new_user in current_users:

        print(f"Sorry we cannot create username for {new_user.title()}, as it already exists.")
    else:
        print(f"New account created for {new_user.title()}.")