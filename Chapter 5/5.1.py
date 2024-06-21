##Conditional tests

#saiyan = 'goku'
#print ("Is saiyan == 'goku'? I predict True.")
#print (saiyan == 'goku')


##You can play with either of the lines below for the conditional loop
saiyan = ['vegeta', 'gohan', 'goku' 'trunks']
#saiyan = ['vegeta', 'gohan', 'goku' 'trunks', 'piccolo']
for fighters in saiyan:
        if fighters == 'piccolo':
            print("Hey, only saiyans in this group!")
##We use "break" to exit the loop entirely if a condition is met.
            break
else:
              print("The Z fighters with saiyan blood will fight.")

#print(f"{saiyan}")