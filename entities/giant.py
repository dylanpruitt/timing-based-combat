from entities.entity import Entity
from random import randint


class Giant(Entity):

    def __init__(self):
        self.name = "Giant"
        self.health = 22 + randint(-6, 6)
        self.max_health = self.health
        self.attack = 1
        self.speed = randint(0, 3)

    def ai(self, player):
        if self.health > 0:
            if self.cooldown == 50 - self.speed:
                random = randint(1, 4)
                if random == 1:
                    self.ai_choice = "attack"
                elif random < 4:
                    self.ai_choice = "defend"
                else:
                    self.ai_choice = "wait_attack"

            if self.cooldown == 0:
                if self.ai_choice == "attack":
                    if not player.defending:
                        player.health -= 4
                    self.cooldown = 200 - self.speed
                elif self.ai_choice == "defend":
                    self.defending = True
                    self.cooldown = 100 - self.speed
                    self.defense_time = 70
                else:
                    self.cooldown = 110 - self.speed
                    self.ai_choice = "attack"
