from entities.entity import Entity
from random import randint


class Slime(Entity):

    def __init__(self):
        self.name = "Slime"
        self.health = 3 + randint(-1, 1)
        self.max_health = self.health
        self.attack = 1
        self.speed = randint(0, 3)

    def ai(self, player):
        if self.health > 0:
            if self.cooldown == 32 - self.speed:
                random = randint(1,4)
                if random == 1:
                    self.ai_choice = "attack"
                elif random < 4:
                    self.ai_choice = "defend"
                else:
                    self.ai_choice = "wait_attack"

            if self.cooldown == 0:
                if self.ai_choice == "attack":
                    if not player.defending:
                        player.health -= 1
                    self.cooldown = 110 - self.speed
                elif self.ai_choice == "defend":
                    self.defending = True
                    self.cooldown = 80 - self.speed
                    self.defense_time = 64
                else:
                    self.cooldown = 30 - self.speed
                    self.ai_choice = "attack"
