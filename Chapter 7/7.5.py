##Movie tickets

message = "\nWelcome to movie phone, please enter your age for ticket pricing."
message += "\n(Enter 'quit' to end the program.)"

while True: 
    #!= 'quit':
#    message = input(prompt)
    number=input(message)
    if number == "quit":
        break

    number = int(number)
    
    if number < 3:
        print("Your price is free!")
        continue

    elif number >= 3 and number <= 12:
        print("Your price will be $10")
        continue

    elif number > 12:
        print("Your price will be $15")
        continue

    else:
        break



#        print()
#    elif message == 'quit':
#        print()


    #print(f"\nAdding {message}, anything else?")