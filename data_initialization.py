from data_models import Hero, Monster, Attack, Location, DamageType, LocationEncounterType

hero = Hero(
    name = 'Hercules',
    max_health = 30,
    attacks = [
        Attack('Stab With Spear', DamageType.PIERCE, 5, True),
        Attack('Cut With Sword', DamageType.SLASH, 5, True),
        Attack('Wrestle', DamageType.GRAPPLE, 3, True),
        Attack('Hit with Club',DamageType.BLUDGEON, 4, True),
        Attack('Pet', DamageType.LOVE, 5, False),
        Attack('Play Fetch', DamageType.LOVE, 4, False),
        Attack('Compliment', DamageType.LOVE, 3, False),
        Attack('Give Treat', DamageType.LOVE, 5, False)
    ])

all_locations = [
    Location(
        name = 'your Overnight Camp',
        description = 'base for resting and recovery',
        encounter_type = LocationEncounterType.REST,
        monsters = []
    ),
    Location(
        name = 'the Tall Grass',
        description = 'fancy words about very tall grass',
        encounter_type = LocationEncounterType.BATTLE,
        monsters = [Monster(
            name = 'the Nemean Lion',
            max_health = 30,
            attacks = [
                Attack('Bite', DamageType.PIERCE, 3, True),
                Attack('Claw', DamageType.SLASH, 2, True)
            ],
            immunities = [DamageType.PIERCE, DamageType.SLASH, DamageType.LOVE],
            is_lethal = True
        )]
    ),
    Location(
        name = 'the Dark Swamp',
        description = 'v wet and slimy',
        encounter_type = LocationEncounterType.BATTLE,
        monsters = [Monster(
            name = 'the Lernaean Hydra',
            max_health = 30,
            attacks = [
                Attack('Bite', DamageType.PIERCE, 3, True),
                Attack('Tail Whip', DamageType.BLUDGEON, 2, True),
                Attack('Poison Breath', DamageType.POISON, 2, True),
            ],
            immunities = [DamageType.POISON, DamageType.GRAPPLE, DamageType.LOVE],
            is_lethal = True
        )]
    ),
    Location(
        name = 'the Gates Of The Underworld',
        description = 'creepy but also cool',
        encounter_type = LocationEncounterType.BATTLE,
        monsters = [Monster(
            name = 'Cerberus',
            max_health = 30,
            attacks = [
                Attack('Sloppy Face Licks', DamageType.LOVE, 3, False),
                Attack('Sad Puppy Eyes', DamageType.LOVE, 4, False)
            ],
            immunities = [],
            is_lethal = False
        )]
    )
]