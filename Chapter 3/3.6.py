### For this we need to do insert, insert and append and print per person on the list.

people = ['Roman Reigns', 'The Rock', 'Rikishi']
hollywood=people.pop(1)
print(f"At my table I'd want to have {people[0]} and {people[1]} but {hollywood} called.")

people.insert(1, 'Usos')
people.append('yoyoyo')
print(f"Well change of plans, {people[1]} are arriving instead and will join {people[0]} and {people[2]}. I forgot to add {people[-1]}.")