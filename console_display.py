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

def display_location_options(available_locations):
    print('\nYou can go to the following areas:')
    for index, location in enumerate(available_locations):
        print(f'{index + 1} - {location}')

def display_full_health_restored(entity):
    print(f'\nAll health for {entity.name} has been restored!')