#4.11

#Establishing the variable for my_pizzas
#Second line copies the list of my_pizzas to friend_pizza 
my_pizzas = ['pepperoni', 'veggie', 'pepperoni and mushrooms']
friends_pizza = my_pizzas [:]

###This is a more long way of doing things
#print("My favourite pizzas are:")
#print(my_pizzas)
#print("\nMy friend's favourite pizzas are:")
#print(friends_pizza)
#print("\nMy mistake, my friend's favourite pizzas are:")
#print(friends_pizza)

##This will append the friend_pizza variable.
friends_pizza.append('sweet peppers')
##First line creates a new sentence line, followed by a sentence
##Second line for loop takes friends_pizza variable as a list
##Third line prints each instance in pizza capitalised.
print("My favourite pizzas are:")
for pizza in my_pizzas[:]:
    print(pizza.title())

##First line creates a new sentence line, followed by a sentence
##Second line for loop takes friends_pizza variable as a list
##Third line prints each instance in friendpizza capitalised.
print("\nMy mistake, my friend's favourite pizzas are:")
for friendpizza in friends_pizza[:]:
    print(friendpizza.title())