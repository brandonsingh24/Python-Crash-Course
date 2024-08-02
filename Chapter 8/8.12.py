
def make_sandwiches (*items):
    """printing sandwich items"""
    print("Making a sandwich with:")
    for item in items:
        print(f"-{item}")

make_sandwiches('pepperoni')
make_sandwiches('pepperoni', 'bacon', 'cheese')
make_sandwiches('tomatoes', 'onions', 'peppers')