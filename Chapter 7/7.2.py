## Restaurant Seating

#Take user input
people=input("How many people are in your dinner group?")

#Take input, pass it through int call; would like to see if str entered do this9
people=int(people)
 
if people >= 8:
    print("\nSorry you'll have to wait")

else:
    print("\nYour table is ready!")