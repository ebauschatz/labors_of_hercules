from data_models import Hero, Monster, Attack, Location, DamageType, LocationEncounterType

hero = Hero(
    name = 'Hercules',
    max_health = 30,
    attacks = [
        Attack('Spear', DamageType.PIERCE, 5, True),
        Attack('Sword', DamageType.SLASH, 5, True),
        Attack('Wrestle', DamageType.GRAPPLE, 3, True),
        Attack('Club',DamageType.BLUDGEON, 4, True),
        Attack('Pet', DamageType.LOVE, 5, False),
        Attack('Play Fetch', DamageType.LOVE, 4, False),
        Attack('Compliment', DamageType.LOVE, 3, False),
        Attack('Give Treat', DamageType.LOVE, 5, False)
    ])

camp_description = '''You have a very comfortable camp bed set up, and after a tasty meal you decide to get a good night's rest. 
    Tomorrow there will be more adventures!'''

tall_grass_description = '''The vegetation in this area is dense and coarse.
    It's almost impossible to see anything below the serenely waving tops of the grasses that graze your shoulders.
    What's that rustling noise?'''

swamp_description = '''It smells wet and musty, and with every step you sink into mud up to your shins. 
    The trees are covered with thick dripping vines that block out most of the sunlight.
    Did something just move in the water?'''

underworld_gates_description = '''A thick stone doorway stands alone near a river.
    Looking through the open arch, you see endless stairs leading down into a dark tunnel.
    Strangely, if you walk around the other side of the arch, the stairs aren't there.
    Why does it suddenly feel like you're being watched?'''

all_locations = [
    Location(
        name = 'your Overnight Camp',
        description = camp_description,
        encounter_type = LocationEncounterType.REST,
        monsters = []
    ),
    Location(
        name = 'the Tall Grass',
        description = tall_grass_description,
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
        description = swamp_description,
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
        description = underworld_gates_description,
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