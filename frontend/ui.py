menu_options = {
    0: 'Exit',
    1: 'Add department',
    2: 'Show departments',
    3: 'Add patient',
    4: 'Sort patients by age',
}

def print_menu():
    """
    Function used to print the menu using the menu_options array
    """
    for option in menu_options.keys():
        print (option, '--', menu_options[option])