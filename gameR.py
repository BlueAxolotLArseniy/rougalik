# #0.001
# import pygame
# import math
# import random
#
# pygame.init()
#
# sc = pygame.display.set_mode((800, 500), pygame.RESIZABLE)
#
# pygame.display.set_caption('GameR')
#
# coordinates1 = None
# coordinates2 = None
#
# FPS = 40
# list_for_squares = []
#
# matrix_of_rooms = [[1 for _ in range(20)],
#                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                    [1 for _ in range(20)]]
#
# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, x, y, filename):
#         super().__init__()
#         self.image = pygame.image.load(filename).convert()
#         self.image.set_colorkey((0, 0, 0))
#         self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
#         self.rect = self.image.get_rect(center=(x, y))
#         self.original_image = self.image
#         self.original_rect = self.rect.copy()
#
#     def update(self, target):
#         rel_x, rel_y = target[0] - self.rect.centerx, target[1] - self.rect.centery
#         self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
#         self.image = pygame.transform.rotate(self.original_image, int(self.angle))
#         self.rect = self.image.get_rect(center=self.rect.center)
#
# class Floor(pygame.sprite.Sprite):
#     def __init__(self, x, y, filename):
#         super().__init__()
#         self.image = pygame.image.load(filename).convert()
#         self.image.set_colorkey((0, 0, 0))
#         self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
#         self.rect = self.image.get_rect(center=(x, y))
#         self.original_image = self.image
#         self.original_rect = self.rect.copy()
#
# class Wall(pygame.sprite.Sprite):
#     def __init__(self, x, y, filename):
#         super().__init__()
#         self.image = pygame.image.load(filename).convert()
#         self.image.set_colorkey((0, 0, 0))
#         self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
#         self.rect = self.image.get_rect(center=(x, y))
#         self.original_image = self.image
#         self.original_rect = self.rect.copy()
#
# class Hero(pygame.sprite.Sprite):
#     def __init__(self, x, y, filename):
#         super().__init__()
#         self.image = pygame.image.load(filename).convert()
#         self.image.set_colorkey((255, 255, 255))
#         self.image = pygame.transform.scale(self.image, (self.image.get_width()*0.8695652174, self.image.get_height()*0.8333333333))
#         self.rect = self.image.get_rect(center=(x, y))
#         self.original_image = self.image
#         self.original_rect = self.rect.copy()
#
# class Gun(pygame.sprite.Sprite):
#     def __init__(self, x, y, filename):
#         super().__init__()
#         self.image = pygame.image.load(filename).convert()
#         self.image.set_colorkey((255, 255, 255))
#         self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
#         self.rect = self.image.get_rect(center=(x, y))
#         self.original_image = self.image
#         self.original_rect = self.rect.copy()
#
#     def update(self, target):
#         rel_x, rel_y = target[0] - self.rect.centerx, target[1] - self.rect.centery
#         self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
#         self.image = pygame.transform.rotate(self.original_image, int(self.angle))
#         self.rect = self.image.get_rect(center=self.rect.center)
#
# rooms = pygame.Surface((800, 500), pygame.SRCALPHA, 32)
# C_rooms = rooms.get_rect()
# C_rooms.x = 0
# C_rooms.y = 0
# rooms = rooms.convert_alpha()
#
# pistol = Gun(0, 0, 'textures/gun/pistol/oldest_pistol.png')
#
# floor = pygame.Surface((800, 500), pygame.SRCALPHA, 32)
# C_floor = [0, 0]
# floor = floor.convert_alpha()
#
# robot = Hero(400, 250, 'textures/heroes/robot/red_robot.png')
#
# def dr_all():
#     point = 0
#     for y in range(50, 450, 20):
#         dr_one_stack(point, y)
#         point += 1
#
# def dr_one_stack(x, y):
#     global matrix_of_rooms, sc
#     point = 200
#     for i in matrix_of_rooms[x]:
#         if i == 1:
#             q = random.randint(0, 4)
#             if q == 0:
#                 wall = Wall(point, y, 'textures/biomes/forest/wall/stone.png')
#                 rooms.blit(wall.image, wall.rect)
#             else:
#                 wall = Wall(point, y, 'textures/biomes/forest/wall/tree.png')
#                 rooms.blit(wall.image, wall.rect)
#         if i == 0:
#             q = random.randint(1, 3)
#             if q == 1:
#                 floor.blit(Wall(point, y+10, 'textures/biomes/forest/floor/dark.png').image,
#                             Wall(point, y+10, 'textures/biomes/forest/floor/dark.png').rect)
#             if q == 2:
#                 floor.blit(Wall(point, y+10, 'textures/biomes/forest/floor/light.png').image,
#                             Wall(point, y+10, 'textures/biomes/forest/floor/light.png').rect)
#             if q == 3:
#                 floor.blit(Wall(point, y+10, 'textures/biomes/forest/floor/medium.png').image,
#                             Wall(point, y+10, 'textures/biomes/forest/floor/medium.png').rect)
#         point += 20
# dr_all()
# clock = pygame.time.Clock()
#
# rooms_mask = pygame.mask.from_surface(rooms)
# floor_mask = pygame.mask.from_surface(floor)
# robot_mask = pygame.mask.from_surface(robot.image)
#
# flLeft = flRight = False
# flUp = flDown = False
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_s: flDown = True
#             elif event.key == pygame.K_w: flUp = True
#             elif event.key == pygame.K_a: flLeft = True
#             elif event.key == pygame.K_d: flRight = True
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_s: flDown = False
#             if event.key == pygame.K_w: flUp = False
#             if event.key == pygame.K_a: flLeft = False
#             if event.key == pygame.K_d: flRight = False
#
#     mouse_pos = pygame.mouse.get_pos()
#
#     sc.fill((0, 0, 0))
#     # rooms.fill((0, 0, 0))
#     sc.blit(floor, C_floor)
#     sc.blit(robot.image, robot.rect)
#     sc.blit(rooms, C_rooms)
#     sc.blit(pistol.image, pistol.rect)
#     pistol.update(pygame.mouse.get_pos())
#     pistol.rect.centerx = robot.rect.centerx
#     pistol.rect.centery = robot.rect.centery
#     # dr_all()
#
#     # if flDown == True:
#     #     C_floor[1] = C_floor[1] - 6
#     #     C_rooms[1] = C_rooms[1] - 6
#     # if flUp == True:
#     #     C_floor[1] = C_floor[1] + 6
#     #     C_rooms[1] = C_rooms[1] + 6
#     # if flLeft == True:
#     #     C_floor[0] = C_floor[0] + 6
#     #     C_rooms[0] = C_rooms[0] + 6
#     # if flRight == True:
#     #     C_floor[0] = C_floor[0] - 6
#     #     C_rooms[0] = C_rooms[0] - 6
#
#     if flDown == True:
#         robot.rect.y += 6
#     if flUp == True:
#         robot.rect.y -= 6
#     if flLeft == True:
#         robot.rect.x -= 6
#     if flRight == True:
#         robot.rect.x += 6
#
#     offset = (int(robot.rect.x - C_rooms.x), int(robot.rect.y - C_rooms.y))
#     if not rooms_mask.overlap_area(robot_mask, offset):
#         coordinates2 = coordinates1
#         coordinates1 = (robot.rect.x, robot.rect.y)
#
#     offset = (int(robot.rect.x - C_rooms.x), int(robot.rect.y - C_rooms.y))
#     if rooms_mask.overlap_area(robot_mask, offset):
#         if flUp == True and flRight == True:
#             offset = (int(robot.rect.x + 6 - C_rooms.x), int(robot.rect.y - C_rooms.y))
#             if not rooms_mask.overlap_area(robot_mask, offset):
#                 robot.rect.x += 6
#             else:
#                 robot.rect.x = coordinates2[0]
#             offset = (int(robot.rect.x - C_rooms.x), int(robot.rect.y - 6 - C_rooms.y))
#             if not rooms_mask.overlap_area(robot_mask, offset):
#                 robot.rect.y -= 6
#             else:
#                 robot.rect.y = coordinates2[1]
#         else:
#             print('пересечение')
#             robot.rect.x = coordinates2[0]
#             robot.rect.y = coordinates2[1]
#
#     print(coordinates1, coordinates2)
#
#     pygame.display.flip()
#     clock.tick(FPS)
#
# pygame.quit()

#0.001
import pygame
import math
import random

pygame.init()

sc = pygame.display.set_mode((800, 500), pygame.RESIZABLE)

pygame.display.set_caption('GameR')

coordinates1 = None
coordinates2 = None

FPS = 40
list_for_squares = []

matrix_of_rooms = [[1 for _ in range(20)],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1 for _ in range(20)]]

lst_of_walls = []

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

class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*0.8695652174, self.image.get_height()*0.8333333333))
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

class Gun(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

    def update(self, target):
        rel_x, rel_y = target[0] - self.rect.centerx, target[1] - self.rect.centery
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(self.angle))
        self.rect = self.image.get_rect(center=self.rect.center)

rooms = pygame.Surface((800, 500), pygame.SRCALPHA, 32)
C_rooms = rooms.get_rect()
C_rooms.x = 0
C_rooms.y = 0
rooms = rooms.convert_alpha()

pistol = Gun(0, 0, 'textures/gun/pistol/oldest_pistol.png')

floor = pygame.Surface((800, 500), pygame.SRCALPHA, 32)
C_floor = [0, 0]
floor = floor.convert_alpha()

robot = Hero(400, 250, 'textures/heroes/robot/red_robot.png')

def dr_all():
    point = 0
    for y in range(50, 450, 20):
        dr_one_stack(point, y)
        point += 1

def dr_one_stack(x, y):
    global matrix_of_rooms, sc
    point = 200
    for i in matrix_of_rooms[x]:
        if i == 1:
            q = random.randint(0, 4)
            if q == 0:
                wall = Wall(point, y, 'textures/biomes/forest/wall/stone.png')
                rooms.blit(wall.image, wall.rect)
                lst_of_walls.append(wall)
            else:
                wall = Wall(point, y, 'textures/biomes/forest/wall/tree.png')
                rooms.blit(wall.image, wall.rect)
                lst_of_walls.append(wall)
        if i == 0:
            q = random.randint(1, 3)
            if q == 1:
                wall = Wall(point, y, 'textures/biomes/forest/floor/dark.png')
                floor.blit(wall.image, wall.rect)
            if q == 2:
                wall = Wall(point, y, 'textures/biomes/forest/floor/light.png')
                floor.blit(wall.image, wall.rect)
            if q == 3:
                wall = Wall(point, y, 'textures/biomes/forest/floor/medium.png')
                floor.blit(wall.image, wall.rect)
        point += 20
dr_all()
clock = pygame.time.Clock()

rooms_mask = pygame.mask.from_surface(rooms)
floor_mask = pygame.mask.from_surface(floor)
robot_mask = pygame.mask.from_surface(robot.image)

flLeft = flRight = False
flUp = flDown = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s: flDown = True
            elif event.key == pygame.K_w: flUp = True
            elif event.key == pygame.K_a: flLeft = True
            elif event.key == pygame.K_d: flRight = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s: flDown = False
            if event.key == pygame.K_w: flUp = False
            if event.key == pygame.K_a: flLeft = False
            if event.key == pygame.K_d: flRight = False

    mouse_pos = pygame.mouse.get_pos()

    if flDown == True:
        robot.rect.y += 6
    if flUp == True:
        robot.rect.y -= 6
    if flLeft == True:
        robot.rect.x -= 6
    if flRight == True:
        robot.rect.x += 6

    for i in lst_of_walls:
        if not i.rect.colliderect(robot.rect):
            coordinates2 = coordinates1
            coordinates1 = (robot.rect.x, robot.rect.y)

    sc.fill((0, 0, 0))
    # rooms.fill((0, 0, 0))
    sc.blit(floor, C_floor)
    sc.blit(robot.image, robot.rect)
    sc.blit(rooms, C_rooms)
    # sc.blit(pistol.image, pistol.rect)
    pistol.update(pygame.mouse.get_pos())
    pistol.rect.centerx = robot.rect.centerx
    pistol.rect.centery = robot.rect.centery
    # dr_all()

    # if flDown == True:
    #     C_floor[1] = C_floor[1] - 6
    #     C_rooms[1] = C_rooms[1] - 6
    # if flUp == True:
    #     C_floor[1] = C_floor[1] + 6
    #     C_rooms[1] = C_rooms[1] + 6
    # if flLeft == True:
    #     C_floor[0] = C_floor[0] + 6
    #     C_rooms[0] = C_rooms[0] + 6
    # if flRight == True:
    #     C_floor[0] = C_floor[0] - 6
    #     C_rooms[0] = C_rooms[0] - 6

    for i in lst_of_walls:
        if i.rect.collidepoint(robot.rect.topright[0]-10, robot.rect.topright[1]):
            print('awd')
            robot.rect.y = coordinates2[1]

    print(coordinates1, coordinates2)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()