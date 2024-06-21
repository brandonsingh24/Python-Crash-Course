# Make an empty list to store people in.
pets = []

# Define some people, and add them to the list.
pet_info = {
    'first_name': 'santas little helper',
    'last_name': 'simpson',
    'age': 5,
    'city': 'springfield',
    }
pets.append(pet_info)

pet_info = {
    'first_name': 'snowball 1',
    'last_name': 'simpson',
    'age': 2,
    'city': 'springfield',
    }
pets.append(pet_info)

pet_info = {
    'first_name': 'snowball 2',
    'last_name': 'simpson',
    'age': 11,
    'city': 'springfield',
    }
pets.append(pet_info)

# Display all of the information in the dictionary.
for pet_info in pets:
    name = f"{pet_info['first_name'].title()} {pet_info['last_name'].title()}"
    age = pet_info['age']
    city = pet_info['city'].title()

    print(f"{name}, of {city}, is {age} years old.")