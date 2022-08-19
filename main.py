import console_display
from data_initialization import hero, all_locations
from data_models import LocationEncounterType

def main():
    console_display.display_welcome_message()
    run_game(hero, all_locations)
    console_display.display_closing_message()

def run_game(hero, locations):
    console_display.display_health_percentage(hero.name, hero.max_health, hero.current_health)
    next_location = select_location_by_name(locations)
    console_display.display_entering_location(next_location)
    run_location_encounter(next_location, hero)

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
        run_monster_battle(current_monster, hero)

def select_current_monster(available_monsters):
    return available_monsters[0]

def restore_all_health(entity):
    entity.current_health = entity.max_health
    console_display.display_full_health_restored(entity)

def run_monster_battle(monster, hero):
    hero_attacks = get_available_attacks(hero.attacks, monster.is_lethal)
    attack(hero, hero_attacks, monster, monster.attacks)

def get_available_attacks(all_attacks, attack_is_lethal):
    return [x for x in all_attacks if x.is_lethal is attack_is_lethal]

def attack(hero, hero_attacks, monster, monster_attacks):
    while monster.current_health > 0:
        console_display.display_health_percentage(hero.name, hero.max_health, hero.current_health)
        console_display.display_health_percentage(monster.name, monster.max_health, monster.current_health)
        console_display.display_attack_names(hero_attacks)
        #todo: input validation
        selected_attack_index = int(input('Please enter the number of the attack you wish to make: ')) - 1
        selected_attack = hero_attacks[selected_attack_index]
        if selected_attack.damage_type in monster.immunities:
            console_display.display_attack_failed(f'{monster.name} is immune to this attack')
            continue
        apply_attack(selected_attack, monster)
    console_display.display_battle_won(monster.name, 'defeated') #change to 'slain' or 'tamed' based on battle type

def apply_attack(attack, target):
    target.current_health -= attack.damage_amount

main()