###Breaking up long print command
#print("test"
#      "ing 123"
#      )

people=[]

basic_info0 = {
    'first_name': 'bart',
    'last_name': 'simpson',
    'age': 10,
    'city': 'springfield'
}

basic_info1 = {
    'first_name': 'lisa',
    'last_name': 'simpson',
    'age': 10,
    'city': 'springfield'
}

basic_info2 = {
    'first_name': 'homer',
    'last_name': 'simpson',
    'age': 40,
    'city': 'springfield'
}

people=[basic_info0, basic_info1, basic_info2]

for firstname in people.items():
    print(f"{firstname}")

#print(f"""My name is {basic_info['first_name'].title()} {basic_info['last_name'].title()}, 
#      I am {basic_info['age']} years old 
#      and I'm from {basic_info['city'].title()}.""")