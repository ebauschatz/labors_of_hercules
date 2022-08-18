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

all_monsters = [
    Monster(
        name = 'the Nemean Lion',
        max_health = 30,
        attacks = [
            Attack('Bite', 'pierce', 3, True),
            Attack('Claw', 'slash', 2, True)
        ],
        immunities = ['pierce', 'slash'],
        location = Location('Tall Grass', 'fancy words about very tall grass')
    ),
    Monster(
        name = 'the Lernaean Hydra',
        max_health = 30,
        attacks = [
            Attack('Bite', 'pierce', 3, True),
            Attack('Tail Whip', 'bludgeon', 2, True),
            Attack('Poison Breath', 'poison', 2, True),
        ],
        immunities = ['grapple'],
        location = Location('Dark Swamp', 'v wet and slimy')
    ),
    Monster(
        name = 'Cerberus',
        max_health = 30,
        attacks = [
            Attack('Sloppy Face Licks', 'poison', False),
            Attack('Sad Puppy Eyes', )
        ],
        immunities = [],
        location = Location('Gates Of The UnderWorld', 'creepy but also cool')
    )
]