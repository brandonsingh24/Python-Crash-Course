###Have to limit guest table to 2 people. Must use pop.

people = ['Roman Reigns', 'The Rock', 'Rikishi']
print(people)
sorry1=people.pop(1)

print(f"Sorry our table can't fit {sorry1} and his ego.")
print(people)

sorry2=people.pop(0)
print(f"You're our tribal chief {sorry2}, you deserve your own table not to sit at just A table.")
print(f"You're still a bad man and you get the table to yourself {people[0]}!")

del people[0]
print(f"No one left except {people} - wait no that's all")