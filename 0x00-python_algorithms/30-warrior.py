'''
Warrior game:
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has Died and Sam is victorious
Game over!
'''
import  random
import math

class Warrior:

    def __init__(self, name = "Warrior", health = 0, attackMax = 0, blockMax = 0):
        self.name = name
        self.health = health
        self.attackMax = attckMax
        self.blockMax = blockMax

    def attack(self):
        attckAmt = self.attackMax * (random.random() + .5)
        return attckAmt

    def block(self):
        blockckAmt = self.blockMax * (random.random() + .5)
        return blockckAmt

class Battle:

    def startFight(self, warrior1, warrior2):

        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over!")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over!")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):

        warriorAAttackAmt = warriorA.attack()
        warriorBBloack = warriorB.block()
        damage2WarriorB = math.ceil(warriorAAttackAmt - warriorBBloack)

        warriorB.health = warriorB.health - damage2WarriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name),
              warriorB.name, damage2WarriorB)
        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has died and {} is victorious".format(warriorB.name, warriorA.name))
            return "Game Over!"
        else:
            return "Fight Again"

def main():
    maximus = Warrior("maximus", 50, 20, 10)

    tila = Warrior("tila", 50, 20, 10)

    battle = battle()

    battle.startFight(maximus,tila)




