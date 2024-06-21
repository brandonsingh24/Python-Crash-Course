###5.9

#names = ['marge', 'maggie', 'bart', 'homer', 'lisa', 'admin']
names = []

for name in names:
    if name == 'admin':
        print(f"Hello, {name.title()}, would you like to see a status report?")

    else:
        print(f"Hello {name.title()}, thank you for logging in again.")

else:
    print("We need to find some users!")