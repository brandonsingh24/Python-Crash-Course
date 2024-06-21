#6.6
polling = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}


coders = ('jen', 'sarah', 'edward', 'phil', 'carlos', 'luke',)

for coder in coders:
    if coder in polling.keys():
        print(f"Thank you {coder.title()}!")
    else:
        print(f"{coder.title()} please do the poll!")