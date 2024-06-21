### Same as 4.11 but for fun wanted to work with range.

numbers = list(range(1, 101))

altnumbers = numbers[:]
altnumbers.extend(range(225, 230))

for num in numbers[:]:
    print(num)

for altnum in altnumbers[:]:
    print(altnum)