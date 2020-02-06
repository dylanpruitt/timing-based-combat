from entities.entity import Entity
from random import randint


class Lizard(Entity):

    def __init__(self):
        self.name = "Lizard"
        self.health = 5 + randint(-3, 1)
        self.max_health = self.health
        self.attack = 2
        self.speed = randint(3, 8)

    def ai(self, player):
        if self.health > 0:
            if self.cooldown == 50 - self.speed:
                random = randint(1,4)
                if random == 1:
                    self.ai_choice = "attack"
                elif random == 2:
                    self.ai_choice = "defend"
                elif random == 3:
                    self.ai_choice = "wait_attack"
                else:
                    self.ai_choice = "quick_attack"

            if self.cooldown == 0:
                if self.ai_choice == "attack":
                    if not player.defending:
                        player.health -= 2
                    self.cooldown = 80 - self.speed
                elif self.ai_choice == "defend":
                    self.defending = True
                    self.cooldown = 65 - self.speed
                    self.defense_time = 36
                elif self.ai_choice == "wait_attack":
                    self.cooldown = 45 - self.speed
                    self.ai_choice = "attack"
                else:
                    if not player.defending:
                        player.health -= 1
                    self.cooldown = 55 - self.speed
