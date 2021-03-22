# Python RPG game ver.3
import random
import math
import time
from pprint import pprint


class Hero:
    def __init__(self, health, attack, defence, level=1):
        self.health = health
        self.attack = attack
        self.defence = defence
        self.name = "Player"
        self.experience = level * 100 - 100
        self.level = level
        self.swordLvl = 1
        self.armourLvl = 1

    def __repr__(self):
        return f"Hero({self.health}, {self.attack}, {self.defence})"

    def __str__(self):
        return f"{self.name}(hp:{self.health}, atk:{self.attackPts}, def:{self.defencePts}, exp:{self.experience}, lvl:{self.level})"

    def getHealth(self):
        return self.health

    def getName(self):
        return self.name

    def getExp(self):
        return self.experience

    @property
    def attackPts(self):
        return self.attack + self.swordLvl * 5

    @property
    def defencePts(self):
        return self.defence + self.armourLvl * 5

    @property
    def equipment(self):
        return f"Sword Lvl - {self.swordLvl}, Armour Lvl - {self.armourLvl}"

    def setHealth(self, value):
        self.health = value

    def setAttack(self, value):
        self.attack = value

    def setDefence(self, value):
        self.defence = value

    def setExp(self, value):
        self.experience = value

    @equipment.deleter
    def equipment(self):
        print("—— You lost your equipment ——\n")
        self.swordLvl = 0
        self.armourLvl = 0

    def isDead(self):
        return False if (self.health > 0) else True

    def updateLvl(self):
        if (self.experience >= 100 * self.level):
            self.level += 1
            self.health = 90 + 10 * self.level
            self.setAttack(self.attack + 5)
            self.setDefence(self.defence + 5)
            print("*** Level Up! ***")
            print(self.equipment)


class Enemy:
    def __init__(self, health, attack, defence):
        self.health = health
        self.attack = attack
        self.defence = defence
        self.name = "Enemy"
        self.experience = math.ceil((self.attack + self.defence + self.health) / 3)

    def __repr__(self):
        return f"Enemy({self.health}, {self.attack}, {self.defence})"

    def __str__(self):
        return f"{self.name}(hp:{self.health}, atk:{self.attackPts}, def:{self.defencePts}, exp:{self.experience})"

    def getHealth(self):
        return self.health

    def getName(self):
        return self.name

    def getExp(self):
        return self.experience

    @property
    def attackPts(self):
        return self.attack

    @property
    def defencePts(self):
        return self.defence

    def setHealth(self, value):
        self.health = value

    def setAttack(self, value):
        self.attack = value

    def setDefence(self, value):
        self.defence = value

    def isDead(self):
        return False if (self.health > 0) else True


def generateEnemy(isBoss):
    if (isBoss):
        health = random.randint(75, 150)
        attack = random.randint(10, 40)
        defence = random.randint(10, 30)
    else:
        health = random.randint(20, 100)
        attack = random.randint(5, 30)
        defence = random.randint(5, 25)
    return Enemy(health, attack, defence)


def attackOpponent(attacker, defender):
    attackValue = random.randint(1, attacker.attackPts)
    hitValue = math.ceil(attackValue - (defender.defencePts / 2) + 5)
    if (hitValue < 0):
        hitValue = 0
    defender.setHealth(defender.getHealth() - hitValue)
    print(f"{attacker.getName()}’s attack took {hitValue} HP")
    if (defender.isDead()):
        print(defender.getName(), "is dead ")


player = Hero(100, 30, 30)


def fight(withBoss=False):
    enemy = generateEnemy(withBoss)

    # pprint(vars(player))
    # pprint(vars(enemy))
    print(player)
    print(enemy)
    print("————")

    while (not enemy.isDead() and not player.isDead()):
        if (not player.isDead()):
            attackOpponent(player, enemy)
        if (not enemy.isDead()):
            attackOpponent(enemy, player)
        else:
            player.setExp(player.getExp() + enemy.getExp())
            player.updateLvl()

    print("————")
    # pprint(vars(player))
    # pprint(vars(enemy))
    print(player)
    print(enemy)
    print("\n\n")


for i in range(3):
    if (not player.isDead()):
        fight()
        time.sleep(2)

print("BOSS FIGHT")
fight(True)

del player.equipment

for i in range(3):
    if (not player.isDead()):
        fight()
        time.sleep(2)
