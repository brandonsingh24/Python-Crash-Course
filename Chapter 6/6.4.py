###Glossary 2

basic_info = {
    'loop': 'having a program go through multiple values for a specific reason',
    'splice': 'access a value in a list',
    'range': 'automating numerical values automatically',
    'del': 'removing a specific value from a list',
    'index': 'the unique position of a value in a list',
##new stuff
    'string': 'formatable text'
}


print("Welcome to the Python Glossary of terms:")

for term in basic_info:
    define = basic_info[term]
    print(f"\n{term.capitalize()}: {define.capitalize()}")

