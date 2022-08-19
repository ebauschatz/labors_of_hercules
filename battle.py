import random
import console_display

def restore_all_health(entity):
    entity.current_health = entity.max_health
    console_display.display_full_health_restored(entity)

def run_battle(opponent, hero):
    hero_attacks = get_available_attacks(hero.attacks, opponent.is_lethal)
    battle_won = attack(hero, hero_attacks, opponent, opponent.attacks)
    return battle_won

def get_available_attacks(all_attacks, attack_is_lethal):
    return [x for x in all_attacks if x.is_lethal is attack_is_lethal]

def attack(hero, hero_attacks, opponent, opponent_attacks):
    while opponent.current_health > 0 and hero.current_health > 0:
        console_display.display_all_health_percentages([hero, opponent])
        #hero attack
        console_display.display_attack_names(hero_attacks)
        #todo: input validation
        selected_attack_index = int(input('Please enter the number of the attack you wish to make: ')) - 1
        selected_attack = hero_attacks[selected_attack_index]
        if selected_attack.damage_type in opponent.immunities:
            console_display.display_attack_failed(f'{opponent.name} is immune to this attack')
            continue
        apply_attack(selected_attack, opponent)
        if opponent.current_health <= 0:
            return True
        #opponent attack
        selected_attack = select_random_attack(opponent_attacks)
        apply_attack(selected_attack, hero)
        if hero.current_health <= 0:
            return False

def apply_attack(attack, target):
    target.current_health -= attack.damage_amount

def select_random_attack(attack_options):
    return random.choice(attack_options)