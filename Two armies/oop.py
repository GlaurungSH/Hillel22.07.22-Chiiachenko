import random
from unit_attributes import warrior_names

"""
Character characteristics:
Strength (Strength) - Affects the damage of melee weapons
Dexterity - Affects both ranged weapon damage and melee weapon damage. Whoever has more dexterity will attack first.
Intelligence (Intelligence) - Affects the damage of magic weapons,
as well as to a small extent the damage of melee weapons and the damage of ranged weapons
Concentration (Focus) - Affects only the effectiveness of staves of priests
Constitution (Constitution) - Affects the number of health points of the character
Durability - Affects the amount of damage taken
"""

"""
Strength
Each 1 point of strength increases the damage bonus for the following melee weapons:
    +1 damage for the Ax;
    +1 damage for Sword and Rapier;
    +1 Spear damage.

Agility
Every 1 point of Agility increases the damage bonus for the following ranged and melee weapons:
    +1 damage for Bow;
    +1 damage for Musket, Rapier and Spear;
    +1 damage for Sword and Axe.

Intelligence
Every 1 point of intelligence increases the damage bonus for the following magic, ranged, and melee weapons:
    +1 damage for Staff of Fire and Ice Glove;
    +1 damage for Bow, Musket.

Concentration
Every 1 point of concentration increases the damage for the healing weapon:
    +1 damage for the Staff of Life.

Body type
Every 1 point of constitution increases the character's maximum health.

Fortitude
Each 1 unit increases the amount of armor of the character"""


class Army:

    def __init__(self):
        self.health = 100
        self.name = random.choice(warrior_names)

    def check_hp(self):
        if self.health <= 0:
            if self in Battle.red_army:
                Battle.red_army.remove(self)
                print(f'Warrior {self.name} from the Red Army died')
            elif self in Battle.blue_army:
                Battle.blue_army.remove(self)
                print(f'Warrior {self.name} from the Blue Army died')


class Battle:
    red_army = []
    blue_army = []

    @staticmethod
    def generator_warriors(input_number_warriors: int):
        number_knights = round(input_number_warriors * 0.4)
        number_mages = round(input_number_warriors * 0.2)
        number_shooters = round(input_number_warriors * 0.3)
        number_priests = input_number_warriors - number_knights - number_mages - number_shooters
        for knight in range(number_knights):
            Battle.red_army.append(Knights())
            Battle.blue_army.append(Knights())
        for mage in range(number_mages):
            Battle.red_army.append(Mage())
            Battle.blue_army.append(Mage())
        for shooter in range(number_shooters):
            Battle.red_army.append(Shooter())
            Battle.blue_army.append(Shooter())
        for priest in range(number_priests):
            Battle.red_army.append(Priest())
            Battle.blue_army.append(Priest())

    @staticmethod
    def attack_generator():
        warrior_red = random.choice(Battle.red_army)
        warrior_blue = random.choice(Battle.blue_army)

        damage = warrior_red.damage()
        warrior_blue.health -= damage
        print(f'{warrior_red.name} attack {warrior_blue.name} damage {damage}, '
              f'{warrior_blue.name} left {warrior_blue.health}')

        damage = warrior_blue.damage()
        warrior_red.health -= damage
        print(f'{warrior_blue.name} attack {warrior_red.name} damage {damage}, '
              f'{warrior_red.name} left {warrior_red.health}')

        warrior_red.check_hp()
        warrior_blue.check_hp()

    @staticmethod
    def bloody_war():
        print('Let the bloody war begin')
        while True:
            if len(Battle.red_army) and len(Battle.blue_army):
                Battle.attack_generator()
            else:
                break

        if not len(Battle.red_army):
            print('Blue army win')
        else:
            print('Red army win')


class Knights(Army):

    def __init__(self):
        super().__init__()
        self.strength = 13
        self.dexterity = 12
        self.physique = 12
        self.durability = 11
        self.health = self.total_hp()

    def damage(self):
        knight_weapon = {'sword': random.randint(35, 45),
                         'axe': random.randint(40, 50),
                         'rapier': random.randint(32, 42),
                         'spear': random.randint(30, 40)
                         }
        knight_selected_weapon = list(random.choice(list(knight_weapon.items())))[0]
        print(f'Knight {self.name} chose weapon {knight_selected_weapon}')

        if knight_selected_weapon == 'sword':
            knight_damage = knight_weapon['sword'] + self.strength + self.dexterity
        elif knight_selected_weapon == 'axe':
            knight_damage = knight_weapon['axe'] + self.strength + self.dexterity
        elif knight_selected_weapon == 'rapier':
            knight_damage = knight_weapon['rapier'] + self.strength + self.dexterity
        elif knight_selected_weapon == 'spear':
            knight_damage = knight_weapon['spear'] + self.strength + self.dexterity

        knight_damage = (knight_damage * random.uniform(1.5, 3)) if (random.randint(0, 10) % 5 == 0) else knight_damage
        return round(knight_damage)

    def total_hp(self):
        knight_armor = {'heavy knight armor': random.randint(20, 30),
                        'knight medium armor': random.randint(15, 19)
                        }
        knight_selected_armor = list(random.choice(list(knight_armor.items())))[0]
        print(f'Knight {self.name} chose armor {knight_selected_armor}')

        if knight_selected_armor == 'heavy knight armor':
            knight_armor_health = self.health + knight_armor['heavy knight armor'] + self.physique + self.durability
        elif knight_selected_armor == 'knight medium armor':
            knight_armor_health = self.health + knight_armor[
                'knight medium armor'] + self.physique + self.durability
        return round(knight_armor_health)


class Mage(Army):

    def __init__(self):
        super().__init__()
        self.dexterity = 13
        self.intelligence = 16
        self.physique = 9
        self.durability = 7
        self.health = self.total_hp()

    def damage(self):
        mage_weapon = {'fire staff': random.randint(25, 55),
                       'ice glove': random.randint(20, 40)
                       }
        mage_selected_weapon = list(random.choice(list(mage_weapon.items())))[0]
        print(f'Mage {self.name} chose weapon {mage_selected_weapon}')

        if mage_selected_weapon == 'fire staff':
            mage_damage = mage_weapon['fire staff'] + self.intelligence
        elif mage_selected_weapon == 'ice glove':
            mage_damage = mage_weapon['ice glove'] + self.intelligence

        mage_damage = (mage_damage * random.uniform(1.5, 3)) if (random.randint(0, 10) % 5 == 0) else mage_damage
        return round(mage_damage)

    def total_hp(self):
        mage_armor = {'barrier': random.randint(9, 14),
                      'mage light armor': random.randint(5, 9),
                      'stone skin': random.randint(10, 15)
                      }
        mage_selected_armor = list(random.choice(list(mage_armor.items())))[0]
        print(f'Mage {self.name} chose armor {mage_selected_armor}')

        if mage_selected_armor == 'barrier':
            mage_armor_health = self.health + mage_armor['barrier'] + self.physique + self.durability
        elif mage_selected_armor == 'mage light armor':
            mage_armor_health = self.health + mage_armor['mage light armor'] + self.physique + self.durability
        elif mage_selected_armor == 'stone skin':
            mage_armor_health = self.health + mage_armor['stone skin'] + self.physique + self.durability
        return round(mage_armor_health)


class Shooter(Army):

    def __init__(self):
        super().__init__()
        self.dexterity = 16
        self.intelligence = 10
        self.physique = 10
        self.durability = 9
        self.health = self.total_hp()

    def damage(self):
        shooter_weapon = {'bow': random.randint(20, 45),
                          'musket': random.randint(25, 60)
                          }
        shooter_selected_weapon = list(random.choice(list(shooter_weapon.items())))[0]
        print(f'Shooter {self.name} chose weapon {shooter_selected_weapon}')

        if shooter_selected_weapon == 'bow':
            shooter_damage = shooter_weapon['bow'] + self.intelligence + self.dexterity
        elif shooter_selected_weapon == 'musket':
            shooter_damage = shooter_weapon['musket'] + self.intelligence + self.dexterity

        shooter_damage = (shooter_damage * random.uniform(1.5, 3)) if (random.randint(0, 10) % 5 == 0) \
            else shooter_damage
        return round(shooter_damage)

    def total_hp(self):
        shooter_armor = {'medium_armor_arrow': random.randint(14, 18),
                         'light_armor_arrow': random.randint(6, 10)
                         }
        shooter_selected_armor = list(random.choice(list(shooter_armor.items())))[0]
        print(f'Shooter {self.name} chose armor {shooter_selected_armor}')

        if shooter_selected_armor == 'medium_armor_arrow':
            shooter_armor_health = self.health + shooter_armor[
                'medium_armor_arrow'] + self.physique + self.durability
        elif shooter_selected_armor == 'light_armor_arrow':
            shooter_armor_health = self.health + shooter_armor[
                'light_armor_arrow'] + self.physique + self.durability
        return shooter_armor_health


class Priest(Army):

    def __init__(self):
        super().__init__()
        self.dexterity = 16
        self.concentration = 15
        self.physique = 10
        self.durability = 9
        self.health = self.total_hp()

    def damage(self):
        priest_weapon = {'staff_of_life': random.randint(26, 50),
                         'staff_of_light': random.randint(21, 49)
                         }
        priest_selected_weapon = list(random.choice(list(priest_weapon.items())))[0]
        print(f'Priest {self.name} chose weapon {priest_selected_weapon}')

        if priest_selected_weapon == 'staff_of_life':
            priest_damage = priest_weapon['staff_of_life'] + self.concentration
        elif priest_selected_weapon == 'staff_of_light':
            priest_damage = priest_weapon['staff_of_light'] + self.concentration

        priest_damage = (priest_damage * random.uniform(1.5, 3)) if (
                    random.randint(0, 10) % 5 == 0) else priest_damage

        if random.randint(0, 10) % 5 == 0:
            if self in Battle.red_army:
                random.choice(Battle.red_army).health += 10
            elif self in Battle.blue_army:
                random.choice(Battle.blue_army).health += 10

        return round(priest_damage)

    def total_hp(self):
        priest_armor = {'shield': random.randint(12, 16),
                        'priest light armor': random.randint(5, 9)
                        }
        priest_selected_armor = list(random.choice(list(priest_armor.items())))[0]
        print(f'Priest {self.name} chose armor {priest_selected_armor}')

        if priest_selected_armor == 'shield':
            priest_armor_health = self.health + priest_armor['shield'] + self.physique + self.durability
        elif priest_selected_armor == 'priest light armor':
            priest_armor_health = self.health + priest_armor['priest light armor'] + self.physique + self.durability
        return round(priest_armor_health)


Battle.generator_warriors(10)
Battle.bloody_war()
