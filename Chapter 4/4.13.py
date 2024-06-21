##4.13

#The tuple features values that can only be overwritten as a whole and not appended.
buffet = ('steak', 'pizza', 'yogurt', 'salmon', 'egg salad')
print ("Today's menu is:")
for menu in buffet:
    print(menu.title())
print("\nI hope you enjoy your meal!")

###This won't work but we want to show why it won't.

#buffet[-1] = "fried rice"


#changing the tuple
buffet = ('steak', 'pizza', 'yogurt', 'salmon', 'egg salad')
print ("Today's menu is:")
for menu in buffet:
    print(menu.title())
print("\nI hope you enjoy your meal!")

buffet = ('grilled chicken', 'pasta', 'yogurt', 'salmon', 'egg salad')
print ("Sorry about the confusion, today's menu actually is:")
for menu in buffet:
    print(menu.title())
print("\nI hope you enjoy our improved selection")

    