from entities.entity import Entity
from random import randint


class Rat(Entity):

    def __init__(self):
        self.name = "Rat"
        self.health = 2 + randint(-1, 0)
        self.max_health = self.health
        self.attack = 1
        self.speed = randint(5, 10)

    def ai(self, player):
        if self.health > 0:
            if self.cooldown == 32 - self.speed:
                random = randint(1,4)
                if random <= 2:
                    self.ai_choice = "attack"
                else:
                    self.ai_choice = "wait_attack"

            if self.cooldown == 0:
                if self.ai_choice == "attack":
                    if not player.defending:
                        player.health -= 1
                    self.cooldown = 70 - self.speed
                else:
                    self.cooldown = 30 - self.speed
                    self.ai_choice = "attack"
