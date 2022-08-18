from data_models import Hero, Monster, Attack, Location

hero = Hero(
    name = 'Hercules',
    max_health = 30,
    attacks = [
        Attack('Stab With Spear', 'pierce', 5, True),
        Attack('Cut With Sword', 'slash', 5, True),
        Attack('Wrestle', 'grapple', 3, True),
        Attack('Hit with Club','bludgeon', 4, True),
        Attack('Pet the Good Doggo', 'love', 5, False),
        Attack('Play Fetch', 'love', 4, False),
        Attack('Compliment the Handsome Doggo', 'love', 3, False),
        Attack('Give Treat', 'love', 5, False)
    ])

all_locations = [
    Location(
        'Overnight Camp',
        'base for resting and recovery',
        []
    ),
    Location(
        'Tall Grass',
        'fancy words about very tall grass',
        [Monster(
            name = 'the Nemean Lion',
            max_health = 30,
            attacks = [
                Attack('Bite', 'pierce', 3, True),
                Attack('Claw', 'slash', 2, True)
            ],
            immunities = ['pierce', 'slash']
        )]
    ),
    Location(
        'Dark Swamp',
        'v wet and slimy',
        [Monster(
            name = 'the Lernaean Hydra',
            max_health = 30,
            attacks = [
                Attack('Bite', 'pierce', 3, True),
                Attack('Tail Whip', 'bludgeon', 2, True),
                Attack('Poison Breath', 'poison', 2, True),
            ],
            immunities = ['grapple']
        )]
    ),
    Location(
        'Gates Of The UnderWorld',
        'creepy but also cool',
        [Monster(
            name = 'Cerberus',
            max_health = 30,
            attacks = [
                Attack('Sloppy Face Licks', 'love', 3, False),
                Attack('Sad Puppy Eyes', 'love', 4, False)
            ],
            immunities = []
        )]
    )
]