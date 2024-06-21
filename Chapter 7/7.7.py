##Movie tickets infinite loop


message = "\nWelcome to movie phone, please enter your age for ticket pricing."
message += "\n(Enter 'quit' to end the program.)"

while True: 
    #!= 'quit':
#    message = input(prompt)
    number=input(message)
        

    number = int(number)
    
    if number < 3:
        print("Your price is free!")
     

    elif number >= 3 and number <= 12:
        print("Your price will be $10")
       

    elif number > 12:
        print("Your price will be $15")
      