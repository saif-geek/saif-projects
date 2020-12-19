import pygame
from projectile import Projectile

#class 1(player)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 4
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/bot1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 580
        self.rect.y = 400

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
    
    def move_up(self):
        self.rect.y -= self.velocity
        self.image = pygame.image.load('assets/bot2.png')
    
    def move_down(self):
        self.rect.y += self.velocity
        self.image = pygame.image.load('assets/bot1.png')

    def scene_1(self):
        background = pygame.image.load('assets/background.jpg')
