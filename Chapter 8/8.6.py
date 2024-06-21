#City Names

def city_country(city, country, population=''):
    """Showcase city/country possible population"""
    city = city.title()
    country = country.title()
    if population:
        city_country_info = f"{city} {country} {population}"
    
    else:
        city_country_info = f"{city} {country}"
    return city_country_info

full_message = city_country('toronto', 'ontario')
print(f"This is {full_message}")    

full_message = city_country('las vegas', 'america', 'with 134411 people.')
print(f"This is {full_message}")   