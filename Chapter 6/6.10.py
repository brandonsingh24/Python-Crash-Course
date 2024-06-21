##

#6.2

favourite_numbers = {
    'matthews': ['34', '69'],
    'nylander': ['88', '6'],
    'tavares': ['10',],
    'rielly': ['44',],
    'knies': ['23',],
}

for name, number in favourite_numbers.items():
    print(f"{name.title()}'s favourite number is:")
    for numbers in number:
        print(f"{numbers}")