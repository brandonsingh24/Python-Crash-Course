###Deli
#

sandwiches = ['tuna', 'veggie', 'ham']
made_sandwiches = [" "]

while sandwiches:
    available_sandwich = sandwiches.pop()
    print(f"Preparing sandwich: {available_sandwich}")
    made_sandwiches.append(available_sandwich)

    ##Displays all sandwiches
    print("\nThe following sandwiches have been finished:")
    for finished_sandwiches in made_sandwiches:
        print(finished_sandwiches)