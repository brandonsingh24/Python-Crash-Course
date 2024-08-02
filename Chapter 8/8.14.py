##Cars

def make_car(manufacturer, model_name, **addons):
    """building a car profile"""
    addons['car name'] = manufacturer
    addons['car type'] = model_name
    return addons
car = make_car('subaru', 'outback', colour='blue', tow_package=True)

print(car)

car = make_car('toyota', 'rav4', colour='black', tow_package=False)

print(car)