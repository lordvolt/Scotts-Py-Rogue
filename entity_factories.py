from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="☻",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

### EARLIEST FLOOR / SPAWN CHANCES NOT USED - SEE THE DICTS AT procgen.py 

monster_rat_small = Actor(
    char="r",
    color=(102, 51, 0),
    name="Small Rat",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=1, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=10),
    verb_attack="scratches",
)

monster_snake_small = Actor(
    char="s",
    color=(204, 255, 51),
    name="Small Snake",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=1, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=10),
    verb_attack="bites",
)

monster_snake_cobra = Actor(
    char="s",
    color=(0, 153, 51),
    name="Cobra Snake",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=2, base_defense=0, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=20),
    verb_attack="bites",
)

monster_orc_lesser = Actor(
    char="o",
    color=(76, 154, 76),
    name="Lesser Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=5, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=30),
)

monster_orc = Actor(
    char="O",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=40),
)

monster_orc_greater = Actor(
    char="O",
    color=(50, 103, 50),
    name="Greater Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=15, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)
"""
orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
    earliest_floor=0,
    spawn_chance=80,
)
"""
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
    earliest_floor=3,
    spawn_chance=15,
)

health_potion = Item(
    char="!",
    color=(127, 0, 255), 
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
)

greater_health_potion = Item(
    char="♥",
    color=(127, 0, 255), 
    name="Greater Health Potion",
    consumable=consumable.HealingConsumable(amount=20),    
)

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0), 
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)

dagger = Item(
    char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger()
)

sword = Item(char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Sword())

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)