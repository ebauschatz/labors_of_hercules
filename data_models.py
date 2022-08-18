class Hero:
    def __init__(self, name, max_health, attacks):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.attacks = attacks

class Monster:
    def __init__(self, name, max_health, attacks, immunities, location):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.attacks = attacks
        self.immunities = immunities
        self.location = location

#enum for damage_type
class Attack:
    def __init__(self, name, damage_type, damage_amount, is_lethal):
        self.name = name
        self.damage_type = damage_type
        self.damage_amount = damage_amount
        self.is_lethal = is_lethal

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description