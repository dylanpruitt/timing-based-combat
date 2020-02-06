import pygame
from entities.entity import Entity
from entities.slime import Slime
from entities.lizard import Lizard
from entities.rat import Rat
from entities.fox import Fox
from entities.giant import Giant

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("new rpg engine")


class Game:
    def __init__(self):
        self.player = Entity()
        self.player.name = "Raymond"
        self.player.target = 1
        self.player.cooldown = 50
        self.looping = True
        self.clock = pygame.time.Clock()


game = Game()


def battle(player, enemies):
    battling = True
    paused = False

    while battling:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                battling = False
                game.looping = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    battling = False
                    game.looping = False
                if event.key == pygame.K_f:
                    if paused:
                        paused = False
                    else:
                        paused = True

        keys = pygame.key.get_pressed()

        if player.health <= 0 or all_enemies_are_dead(enemies):
            battling = False

        if keys[pygame.K_a]:
            if player.cooldown == 0:
                if not enemies[player.target-1].defending:
                    enemies[player.target-1].health -= player.attack
                player.cooldown = 80 - player.speed
        if keys[pygame.K_s]:
            if player.cooldown == 0:
                player.defending = True
                player.defense_time = 40
                player.cooldown = 54 - player.speed
        if keys[pygame.K_1]:
            player.target = 1
        if keys[pygame.K_2] and len(enemies) > 1:
            player.target = 2
        if keys[pygame.K_3] and len(enemies) > 2:
            player.target = 3

        if not paused:
            if player.cooldown > 0:
                player.cooldown -= 1
            if player.defense_time > 0:
                player.defense_time -= 1
            else:
                player.defending = False

        screen.fill(BLACK)

        render_player_stats(player)

        render_enemy_stats(enemies)

        if paused:
            font = pygame.font.Font(None, 70)
            text = font.render("PAUSED", 1, RED)
            screen.blit(text, (150, 250))

        for i in range(len(enemies)):
            if not paused:
                enemies[i].ai(player)

                if enemies[i].cooldown > 0:
                    enemies[i].cooldown -= 1

                if enemies[i].defense_time > 0:
                    enemies[i].defense_time -= 1
                else:
                    enemies[i].defending = False

        pygame.display.flip()

        game.clock.tick(30)

    if player.health > 0:
        player.health = player.max_health


def all_enemies_are_dead(enemies):
    enemies_are_dead = True
    for enemy in enemies:
        if enemy.health > 0:
            enemies_are_dead = False

    return enemies_are_dead


def render_player_stats(player):
    font = pygame.font.Font(None, 45)
    text = font.render(player.name, 1, RED)
    screen.blit(text, (10, 10))
    text = font.render(str(player.health) + " / " + str(player.max_health), 1, RED)
    screen.blit(text, (10, 40))
    text = font.render(str(player.cooldown), 1, WHITE)
    screen.blit(text, (10, 70))
    if player.defending:
        font = pygame.font.Font(None, 30)
        text = font.render("defending", 1, WHITE)
        screen.blit(text, (10, 100))


def render_enemy_stats(enemies):
    for i in range(len(enemies)):
        font = pygame.font.Font(None, 45)
        text = font.render(enemies[i].name, 1, RED)
        screen.blit(text, (350, 10 + 150 * i))
        if i == game.player.target - 1:
            text = font.render("<", 1, WHITE)
            screen.blit(text, (480, 10 + 150 * i))
        text = font.render(str(enemies[i].health) + " / " + str(enemies[i].max_health), 1, RED)
        screen.blit(text, (350, 40 + 150 * i))
        text = font.render(str(enemies[i].cooldown), 1, WHITE)
        screen.blit(text, (350, 70 + 150 * i))
        font = pygame.font.Font(None, 30)
        if enemies[i].defending:
            text = font.render("defending", 1, WHITE)
            screen.blit(text, (350, 100 + 150 * i))
        text = font.render(str(enemies[i].ai_choice), 1, WHITE)
        screen.blit(text, (350, 125 + 150 * i))


def player_choose_reward():
    reward_chosen = False

    while not reward_chosen and game.looping:
        screen.fill(BLACK)

        font = pygame.font.Font(None, 45)
        text = font.render("Choose a reward:", 1, RED)
        screen.blit(text, (150,10))

        font = pygame.font.Font(None, 45)
        text = font.render("1 : +2 HP", 1, RED)
        screen.blit(text, (50, 50))

        font = pygame.font.Font(None, 45)
        text = font.render("2 : +2 SPEED", 1, RED)
        screen.blit(text, (50, 100))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.looping = False
                reward_chosen = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.looping = False
                    reward_chosen = True
                if event.key == pygame.K_1:
                    game.player.max_health += 2
                    game.player.health = game.player.max_health
                    reward_chosen = True
                if event.key == pygame.K_2:
                    game.player.speed += 2
                    reward_chosen = True


def loop():
    battle_number = 0

    encounter_1 = [Rat(), Rat()]
    encounter_2 = [Slime()]
    encounter_3 = [Slime(), Rat(), Rat()]
    encounter_4 = [Slime(), Slime()]
    encounter_5 = [Lizard()]
    encounter_6 = [Fox(), Rat()]
    encounter_7 = [Fox(), Lizard()]
    encounter_8 = [Lizard(), Lizard()]
    encounter_9 = [Fox(), Fox(), Fox()]
    encounter_10 = [Giant()]
    encounters = [encounter_1, encounter_2, encounter_3, encounter_4, encounter_5, encounter_6, encounter_7,
                  encounter_8, encounter_9, encounter_10]

    while game.looping:

        pygame.display.set_caption("new rpg engine : encounter " + str(battle_number + 1))
        battle(game.player, encounters[battle_number])

        if game.player.health <= 0:
            game.looping = False
        else:
            player_choose_reward()
            battle_number += 1
            print(battle_number)

        if battle_number == 10:
            while game.looping:
                screen.fill(BLACK)

                font = pygame.font.Font(None, 45)
                text = font.render("YOU WIN:", 1, RED)
                screen.blit(text, (150, 250))
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game.looping = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game.looping = False


loop()
pygame.quit()
