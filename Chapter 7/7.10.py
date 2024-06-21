#

responses = {}

while True:
    name = input("\nWhat is your name? ")
    response = input("Which place would you like to visit?")

#Storing responses in dictionary
    responses[name] = response

#Find out if anyone else is going to take the poll

    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat.lower() == 'no':
        break

#Polling is complete. Show the results
print("\n Results")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")
