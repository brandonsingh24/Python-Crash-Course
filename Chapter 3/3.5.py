### Rock couldn't make it to dinner

people = ['Roman Reigns', 'The Rock', 'Rikishi']
hollywood=people.pop(1)
print(f"At my table I'd want to have {people[0]} and {people[1]} but {hollywood} called.")

people.insert(1, 'Usos')
print(f"Well change of plans, {people[1]} are arriving instead and will join {people[0]} and {people[2]}.")

#### OR we can do this easier by just modifying the value itself rather than insert.

print(f"{people}.") 
people[1] = 'John Cena'

print( f"Everyone coming to dinner are as follows, {people[0]}, {people[1]} and {people[2]}.")

### Just finally let's see the final value

print(people)