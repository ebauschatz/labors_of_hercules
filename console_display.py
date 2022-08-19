import math

def display_welcome_message():
    print('''\nWelcome to the game!
    You will play as the mighty hero Hercules, and adventure through three of his famous Labors.
    To begin, choose an area to explore and see what happens!''')

def display_closing_message():
    print('''\nCongratulations on completing the game!
    All of your enemies have been defeated (or befriended) and there is peace in all the land!''')

def display_health_percentage(entity_name, max_health, current_health, display_with_newline = False):
    if display_with_newline is True:
        print()
    health_percentage = int(math.ceil(current_health / max_health * 100))
    print(f'The current health of {entity_name} is: {health_percentage}%')

def display_all_health_percentages(entities):
    print()
    for entity in entities:
        display_health_percentage(entity.name, entity.max_health, entity.current_health, False)

def display_full_health_restored(entity):
    print(f'\nAll health for {entity.name} has been restored!')

def display_all_list_options(options_list):
    for index, location in enumerate(options_list):
        print(f'{index + 1} - {location[0].upper() + location[1:]}')

def display_attack_names(attacks):
    print('\nYou can make the following attacks:')
    attack_names = [x.name for x in attacks]
    display_all_list_options(attack_names)

def display_attack_failed(failure_reason):
    print(f'\nThe attack did no damage because {failure_reason}.')

def display_battle_won(opponent_name, victory_action):
    print(f'\nVictory! You have {victory_action} {opponent_name}!')

def display_location_options(available_locations):
    print('\nYou can go to the following areas:')
    display_all_list_options(available_locations)

def display_entering_location(location):
    print(f'''\nYou enter {location.name}.
    {location.description}''')

def display_entity_encountered(entity_name):
    print(f'\nYou encountered {entity_name}!')