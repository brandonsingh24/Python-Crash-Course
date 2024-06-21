##Pizza toppings

prompt = "\nWhat pizza toppings do you want?"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    if message == 'quit':
        break
    
    print(f"\nAdding {message}, anything else?")
##Would like to make the toppings a list that incrementally adds toppings