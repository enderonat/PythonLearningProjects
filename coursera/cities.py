def place_name(city, country, population=''):

    if population:
        name = f'{city},{country} - population {population}'

    else:
        name = f'{city},{country}'
    return name.title()
