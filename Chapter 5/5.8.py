###5.8

names = ['marge', 'maggie', 'bart', 'homer', 'lisa', 'admin']

for name in names:
    if name == 'admin':
        print(f"Hello, {name.title()}, would you like to see a status report?")

    else:
        print(f"Hello {name.title()}, thank you for logging in again.")