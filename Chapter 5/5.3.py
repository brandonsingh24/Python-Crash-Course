##5.3
alien_colour = ['green', 'yellow', 'red']
shotdown = 'green'
shotdown2 = 'purple'
#if shotdown in alien_colour:
#    print ("You earned 5 points!")

#elif 'yellow' in alien_colour:
#    print ("You earned 5 points!")
#elif 'red' in alien_colour:
#    print ("You earned 5 points!")

### where it fails
alien_colour = ['green', 'yellow', 'red']
shotdown = 'purple'
if shotdown in alien_colour:
    print ("You earned 5 points!")
