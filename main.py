import console_display
from data_initialization import hero, all_locations

def main():
    console_display.display_welcome_message()
    run_game(hero, all_locations)
    console_display.display_closing_message()

def run_game(hero, locations):
    console_display.display_health_percentage(hero.name, hero.max_health, hero.current_health)
    next_location = select_location_by_name(locations)
    enter_location(next_location, hero)

#todo: safeguard against invalid input
#only returns first matching 
def select_location_by_name(locations):
    location_names = [x.name for x in locations]
    console_display.display_location_options(location_names)
    selected_location_index = int(input('Please enter the number of the area you wish to go to: ')) - 1
    return locations[selected_location_index]

def enter_location(location, hero):
    if location.name == 'Overnight Camp':
        restore_all_health(hero)

def restore_all_health(entity):
    entity.current_health = entity.max_health
    console_display.display_full_health_restored(entity)

main()