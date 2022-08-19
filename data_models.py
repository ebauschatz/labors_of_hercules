from enum import Enum

class Hero:
    def __init__(self, name, max_health, attacks):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.attacks = attacks

class Monster:
    def __init__(self, name, max_health, attacks, immunities, is_lethal):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.attacks = attacks
        self.immunities = immunities
        self.is_lethal = is_lethal

class Attack:
    def __init__(self, name, damage_type, damage_amount, is_lethal):
        self.name = name
        self.damage_type = damage_type
        self.damage_amount = damage_amount
        self.is_lethal = is_lethal

class Location:
    def __init__(self, name, description, encounter_type, monsters):
        self.name = name
        self.description = description
        self.encounter_type = encounter_type
        self.monsters = monsters

class DamageType(Enum):
    PIERCE = 1
    SLASH = 2
    BLUDGEON = 3
    POISON = 4
    LOVE = 5
    GRAPPLE = 6

class LocationEncounterType(Enum):
    REST = 1
    BATTLE = 2