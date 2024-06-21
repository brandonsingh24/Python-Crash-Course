#


cities = {
    'toronto': {
        'country': 'canada',
        'population': '2.93 million',
        'fact': 'leafs'
        },

    'calgary': {
        'country': 'canada',
        'population': '1.33 million',
        'fact': 'flames'
        },

    'vancouver': {
        'country': 'canada',
        'population': '675,200 thousand',
        'fact': 'canucks'
        },
}

print("Of the following cities and countries their population and hockey team is:")
for city, city_info in cities.items():
    print(f"{city.title()}, {city_info['country'].title()}, {city_info['population']}, {city_info['fact'].title()}")


