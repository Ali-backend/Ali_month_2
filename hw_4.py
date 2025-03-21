from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    HEAL = 1
    BOOST = 2
    CRITICAL_DAMAGE = 3
    BLOCK_DAMAGE_AND_REVERT = 4
    REVIVAL = 5
    HACK = 6
    SAITAMA = 7
    STUN = 8


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.name} health: {self.health} damage: {self.damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if (hero.ability == SuperAbility.BLOCK_DAMAGE_AND_REVERT and
                        self.defence != SuperAbility.BLOCK_DAMAGE_AND_REVERT):
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coefficient = randint(2, 5)
        boss.health -= (self.damage * coefficient)
        print(f'Warrior {self.name} hits critically: {(self.damage * coefficient)} power')


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.REVIVAL)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0 and hero != self:
                hero.health += self.health
                self.health -= self.health
                print(f'Witcher {self.name} revival {hero.name}')
                break


class Magic(Hero):
    def __init__(self, name, health, damage, boost):
        super().__init__(name, health, damage, SuperAbility.BOOST)
        self.__boost = boost

    def apply_super_power(self, boss, heroes):
        # TODO Here will be implementation of boosting
        for hero in heroes:
            if hero != self and hero.damage != 0 and hero.health != 0:
                hero.damage += self.__boost


class Hacker(Hero):
    def __init__(self, name, health, damage, hack):
        super().__init__(name, health, damage, SuperAbility.HACK)
        self.__hack = hack

    def apply_super_power(self, boss, heroes):
        if round_number % 2 == 0:
            hero = choice(heroes)
            boss.health -= self.__hack
            hero.health += self.__hack
            print(f'Hacker {self.name} hacked {self.__hack}')


class King(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAITAMA)

    def apply_super_power(self, boss, heroes):
        chance = randint(1, 10)
        if chance == 5:
            boss.health -= boss.health
            print(f'King {self.name} calling Saitama!')


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.STUN)

    def apply_super_power(self, boss, heroes):
        chance = randint(1, 4)
        if chance == 2:
            boss.damage = 0
            print(f'{self.name} stunning boss')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage}')


round_number = 0


def show_statistics(boss, heroes):
    print(f'ROUND {round_number} ------------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def start_game():
    boss = Boss('Tanos', 1000, 50)
    warrior_1 = Warrior('Thor', 290, 10)
    warrior_2 = Warrior('Hercules', 280, 15)
    magic = Magic('Strange', 270, 20, 5)
    doc = Medic('Aibolit', 250, 5, 15)
    assistant = Medic('Junior', 300, 5, 5)
    berserk = Berserk('Jonathan', 260, 10)
    hacker = Hacker('Maga', 270, 5, 10)
    king = King('Rudolf', 250, 0)
    thor = Thor('Thor', 280, 10)
    witcher = Witcher('Loku', 270, 0)

    heroes_list = [warrior_1, warrior_2, magic, assistant, berserk, doc, hacker, king, thor, witcher]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
