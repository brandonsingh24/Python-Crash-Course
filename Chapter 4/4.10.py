###4.10

fur = ['dogs', 'cats', 'rabbits', 'parrot', 'mice']

print("The first three items in the list are:")
for animals in fur[:3]:
    print(animals.title())


print("Three items from the middle of the list are:")
for animals in fur[2:5]:
    print(animals.title())

print("The last three items in the list are:")
for animals in fur[-3:]:
    print(animals.title())

