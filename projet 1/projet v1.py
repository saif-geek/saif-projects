import pygame
import random
from game import Game
from player import Player

pygame.init()

res = (1366, 705)
screen = pygame.display.set_mode(res, pygame.RESIZABLE)
pygame.display.set_caption("TUTO")
background = pygame.image.load('assets/main.background.jpg')
background = pygame.transform.scale(background, (1366, 705))
player =  Player()
game = Game()
black_color = (0, 0, 0)
blue_color = (96, 60, 255)
red_color = (255, 0, 0)
screen.fill(blue_color)
xpos = 0
ypos = 0

launched = True
while launched:
    pygame.display.flip()
    screen.blit(background, [xpos, ypos])
    screen.blit(player.image, player.rect)
    if game.pressed.get(pygame.K_d) and player.rect.x + player.rect.width < 1396:
        player.move_right()
    elif game.pressed.get(pygame.K_q) and player.rect.x > -10:
        player.move_left()
    elif game.pressed.get(pygame.K_s) and player.rect.y + player.rect.width < 810:
        player.move_down()
    elif game.pressed.get(pygame.K_z) and player.rect.y > -10:
        player.move_up()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_ESCAPE:
                launched = False

            if event.key == pygame.K_F11:
                screen = pygame.display.set_mode(res, pygame.FULLSCREEN)

            if event.key == pygame.K_F12:
                screen = pygame.display.set_mode(res)

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False