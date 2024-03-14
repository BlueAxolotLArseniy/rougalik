#v0.001
import pygame
import math

pygame.init()

sc = pygame.display.set_mode((800, 500), pygame.RESIZABLE)

pygame.display.set_caption('GameR')

FPS = 40

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

test_bullet = Bullet(400, 250, 'textures/gun/bullet/red/rectangle.png')

def rotate_for_mouse():
    global test_bullet
    mx, my = pygame.mouse.get_pos()
    rel_x, rel_y = mx - test_bullet.rect.x, my - test_bullet.rect.y
    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    test_bullet.image = pygame.transform.rotate(test_bullet.original_image, int(angle))
    test_bullet.rect = test_bullet.image.get_rect(center=test_bullet.rect.center)

clock = pygame.time.Clock()
whilee = False
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            whilee = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass
    rotate_for_mouse()
    sc.fill((50, 50, 50))
    sc.blit(test_bullet.image, test_bullet.rect)

    if whilee == True: break
    pygame.display.update()
