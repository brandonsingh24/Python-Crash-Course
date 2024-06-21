###Deli2
#

sandwiches = ['pastrami', 'tuna', 'pastrami', 'veggie', 'ham', 'pastrami']
made_sandwiches = [" "]

while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')
print("Out of pastrami!")

while sandwiches:
    available_sandwich = sandwiches.pop()
    print(f"Preparing sandwich: {available_sandwich}")
    made_sandwiches.append(available_sandwich)

    ##Displays all sandwiches
    print("\nThe following sandwiches have been finished:")
    for finished_sandwiches in made_sandwiches:
        print(finished_sandwiches)