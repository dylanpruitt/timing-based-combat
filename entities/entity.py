class Entity:

    name = "default"
    health = 8
    max_health = 8
    attack = 1
    speed = 1
    cooldown = 100
    defending = False
    defense_time = 0
    ai_choice = "none"

    def __init__(self):
        pass

    def ai(self, player):
        raise NotImplementedError("ai not implemented")
