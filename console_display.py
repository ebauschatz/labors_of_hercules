import math

def display_welcome_message():
    print('''\nWelcome to the game!
    You will play as the mighty hero Hercules, and adventure through three of his famous Labors.
    To begin, choose an area to explore and see what happens!''')

def display_closing_message():
    print('''\nCongratulations on completing the game!
    All of your enemies have been defeated (or befriended) and there is peace in all the land!''')

def display_health_percentage(entity_name, max_health, current_health):
    health_percentage = int(math.ceil(current_health / max_health * 100))
    print(f'\nThe current health of {entity_name} is: {health_percentage}%')

def display_full_health_restored(entity):
    print(f'\nAll health for {entity.name} has been restored!')

def display_all_list_options(options_list):
    for index, location in enumerate(options_list):
        print(f'{index + 1} - {location[0].upper() + location[1:]}')

def display_attack_names(attacks):
    print('\nYou can make the following attacks:')
    attack_names = [x.name for x in attacks]
    display_all_list_options(attack_names)

def display_location_options(available_locations):
    print('\nYou can go to the following areas:')
    display_all_list_options(available_locations)

def display_entering_location(location):
    print(f'''\nYou enter {location.name}.
    {location.description}''')

def display_entity_encountered(entity_name):
    print(f'\nYou encountered {entity_name}!')