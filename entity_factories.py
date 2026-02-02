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
    longname="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=2, dodge_diceroll="1d8+1"),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

### EARLIEST FLOOR / SPAWN CHANCES NOT USED - SEE THE DICTS AT procgen.py 

monster_rat_small = Actor(
    char="r",
    color=(102, 51, 0),
    name="Small Rat",
    longname="Small Rat",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=1, base_defense=0, base_power=3, atk_diceroll="1d6"),
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
    fighter=Fighter(hp=1, base_defense=0, base_power=3, atk_diceroll="1d6"),
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
    fighter=Fighter(hp=2, base_defense=0, base_power=4, atk_diceroll="2d4"),
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
    fighter=Fighter(hp=5, base_defense=0, base_power=3, atk_diceroll="1d8"),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=30),
)

monster_orc = Actor(
    char="O",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3, atk_diceroll="1d10"),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=40),
)

monster_orc_greater = Actor(
    char="O",
    color=(50, 103, 50),
    name="Greater Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=15, base_defense=0, base_power=3, atk_diceroll="1d12"),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)

troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4, atk_diceroll="2d8"),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

item_potion_health_lesser = Item(
    char="♥",
    color=(102, 0, 0), 
    name="Lesser Health Potion",
    longname="Health Potion (1d6+4)",
    consumable=consumable.HealingConsumable(diceroll="1d6+4"),
)

item_potion_health_greater = Item(
    char="♥",
    color=(204, 0, 0), 
    name="Greater Health Potion",
    longname="Greater Health Potion (1d10+6)",
    consumable=consumable.HealingConsumable(diceroll="1d10+6"),    
)

"""
lightning_scroll = Item(
    char="≈",
    color=(255, 255, 0), 
    name="Lightning Scroll",
    longname="Lightning Scroll (5Rng)",
    consumable=consumable.LightningDamageConsumable(dmg_diceroll="3d6+6", maximum_range=5),
)
"""

item_scroll_lighting_v2 = Item(
    char="≈",
    color=(255, 255, 0), 
    name="Lightning Scroll v2",
    longname="Lightning Scroll v2 (5Rng)",
    consumable=consumable.AutoProjectileDamageConsumable(dmg_diceroll="3d6+6", maximum_range=5, projectiletext="Lightning Bolt"),
)

item_scroll_magicmissle = Item(
    char="≈",
    color=(255, 102, 204),
    name="Magic Missle Scroll",
    longname="Magic Missle (Tgt)",
    consumable=consumable.TargetedProjectileDamageConsumable(dmg_diceroll="2d6", maximum_range=5, projectiletext="Magic Missle"),
)

item_scroll_confusion = Item(
    char="≈",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

item_scroll_fireball = Item(
    char="≈",
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