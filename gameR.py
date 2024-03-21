#0.001
import pygame
import math
import random

pygame.init()

sc = pygame.display.set_mode((800, 500), pygame.RESIZABLE)

pygame.display.set_caption('GameR')

FPS = 40
list_for_squares = []

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

    def update(self, target):
        rel_x, rel_y = target[0] - self.rect.centerx, target[1] - self.rect.centery
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(self.angle))
        self.rect = self.image.get_rect(center=self.rect.center)

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

def dr_all():
    for x in range(200, 600, 20):
        for y in range(50, 450, 20):
            sc.blit(Wall(x, y, 'textures/biomes/forest/wall/stone.png').image,
                    Wall(x, y, 'textures/biomes/forest/wall/stone.png').rect)

def draw_room():
    sc.blit(Wall(400, 250, 'textures/biomes/forest/wall/stone.png').image,
            Wall(400, 250, 'textures/biomes/forest/wall/stone.png').rect)

    sc.blit(Wall(420, 250, 'textures/biomes/forest/wall/stone.png').image,
            Wall(420, 250, 'textures/biomes/forest/wall/stone.png').rect)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pass

    mouse_pos = pygame.mouse.get_pos()

    sc.fill((50, 50, 50))
    dr_all()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()