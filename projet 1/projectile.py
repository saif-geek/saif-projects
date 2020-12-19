import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 6
        self.player = player
        self.image = pygame.image.load('assets/boule.png')
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 130
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        if self.rect.x > 1366:
            self.remove()