import console_display
from data_initialization import hero, all_locations
from data_models import LocationEncounterType
from battle import run_battle, restore_all_health

def main():
    console_display.display_welcome_message()
    run_game(hero, all_locations)
    console_display.display_closing_message()

def run_game(hero, locations):
    while len([x for x in locations if x.encounter_type != LocationEncounterType.REST]) > 0:
        console_display.display_health_percentage(hero.name, hero.max_health, hero.current_health, True)
        next_location = select_location_by_name(locations)
        console_display.display_entering_location(next_location)
        run_location_encounter(next_location, hero)
        complete_location_encounter_aftermath(locations)

#todo: safeguard against invalid input
#only returns first matching location
def select_location_by_name(locations):
    location_names = [x.name for x in locations]
    console_display.display_location_options(location_names)
    selected_location_index = int(input('Please enter the number of the area you wish to go to: ')) - 1
    return locations[selected_location_index]

def run_location_encounter(location, hero):
    if location.encounter_type == LocationEncounterType.REST:
        restore_all_health(hero)
        return
    elif location.encounter_type == LocationEncounterType.BATTLE:
        current_monster = select_current_monster(location.monsters)
        console_display.display_entity_encountered(current_monster.name)
        battle_won = run_battle(current_monster, hero)
        if battle_won is True:
            console_display.display_battle_won(current_monster.name, 'defeated') #change to 'slain' or 'tamed' based on battle type
            location.monsters.remove(current_monster)
        else:
            print('Go home and rest')
            restore_all_health(hero)
            restore_all_health(current_monster)

def select_current_monster(available_monsters):
    return available_monsters[0]

def complete_location_encounter_aftermath(locations):
    for location in locations:
        if location.encounter_type == LocationEncounterType.REST:
            continue
        elif location.encounter_type == LocationEncounterType.BATTLE and len(location.monsters) == 0:
            locations.remove(location)

main()