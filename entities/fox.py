from entities.entity import Entity
from random import randint


class Fox(Entity):

    def __init__(self):
        self.name = "Fox"
        self.health = 5 + randint(-3, 2)
        self.max_health = self.health
        self.attack = 1
        self.speed = randint(0, 10)

    def ai(self, player):
        if self.health > 0:
            if self.cooldown == 50 - self.speed:
                random = randint(1, 4)
                if random == 1:
                    self.ai_choice = "attack"
                elif random < 4:
                    self.ai_choice = "defend"
                else:
                    self.ai_choice = "speed_up"

            if self.cooldown == 0:
                if self.ai_choice == "attack":
                    if not player.defending:
                        player.health -= 1
                    self.cooldown = 110 - self.speed
                elif self.ai_choice == "defend":
                    self.defending = True
                    self.cooldown = 80 - self.speed
                    self.defense_time = 70 - self.speed
                else:
                    self.cooldown = 100 - self.speed
                    self.speed += 1
