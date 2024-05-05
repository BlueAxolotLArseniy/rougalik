import pygame
import math
import random

pygame.init()

sc = pygame.display.set_mode((800, 500), pygame.RESIZABLE)

pointQ = None
yQ = None

player_direction_right = True
player_direction_left = False

speed_player = 6

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
        self.rect = self.image.get_rect(center=(x, y-10))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = pygame.Rect((x-10, y-10, 20, 20))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*0.8695652174*2, self.image.get_height()*0.8333333333*2))
        self.rect = pygame.Rect((x-20, y, 19, 19))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] - self.rect.centerx > 0:
            self.image = pygame.transform.flip(self.original_image, True, False)
        else:
            self.image = self.original_image

class Gun(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()

    def update(self, robot_pos):
        rel_x, rel_y = pygame.mouse.get_pos()[0] - robot_pos[0], pygame.mouse.get_pos()[1] - robot_pos[1]
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(self.angle))
        self.rect = self.image.get_rect(center=self.rect.center)

rooms = pygame.Surface((800, 500), pygame.SRCALPHA, 32)
C_rooms = rooms.get_rect()
C_rooms.x = 0
C_rooms.y = 0
rooms = rooms.convert_alpha()

pistol = Gun(0, 0, 'textures/gun/pistol/p250.png')
pistolR = Gun(0, 0, 'textures/gun/pistol/p250R.png')

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
    global matrix_of_rooms, sc, pointQ, yQ
    point = 200
    for i in matrix_of_rooms[x]:
        if i == 1:
            q = random.randint(0, 4)
            if q == 0:
                wall = Wall(point, y, 'textures/biomes/forest/wall/stone.png')
                rooms.blit(wall.image, wall.rect)
                lst_of_walls.append(wall)
                pointQ = point
                yQ = y
                pygame.draw.rect(sc, (255, 255, 255), (point-10, y-10, 20, 20), 5)
            else:
                wall = Wall(point, y, 'textures/biomes/forest/wall/tree.png')
                rooms.blit(wall.image, wall.rect)
                lst_of_walls.append(wall)
                pointQ = point
                yQ = y
                pygame.draw.rect(sc, (255, 255, 255), (point - 10, y - 10, 20, 20), 5)
        if i == 0:
            q = random.randint(1, 3)
            if q == 1:
                wall = Floor(point, y+10, 'textures/biomes/forest/floor/dark.png')
                floor.blit(wall.image, wall.rect)
            if q == 2:
                wall = Floor(point, y+10, 'textures/biomes/forest/floor/light.png')
                floor.blit(wall.image, wall.rect)
            if q == 3:
                wall = Floor(point, y+10, 'textures/biomes/forest/floor/medium.png')
                floor.blit(wall.image, wall.rect)
        point += 20
dr_all()
clock = pygame.time.Clock()

rooms_mask = pygame.mask.from_surface(rooms)
floor_mask = pygame.mask.from_surface(floor)
robot_mask = pygame.mask.from_surface(robot.image)

flLeft = flRight = False
flUp = flDown = False
flShift = False

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
            elif event.key == pygame.K_LSHIFT: flShift = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s: flDown = False
            if event.key == pygame.K_w: flUp = False
            if event.key == pygame.K_a: flLeft = False
            if event.key == pygame.K_d: flRight = False
            if event.key == pygame.K_LSHIFT: flShift = False

    mouse_pos = pygame.mouse.get_pos()


    if flDown == True:
        robot.rect.y += speed_player
    if flUp == True:
        robot.rect.y -= speed_player
    if flLeft == True:
        robot.rect.x -= speed_player
    if flRight == True:
        robot.rect.x += speed_player
    if flShift == True:
        speed_player = 2
    if flShift != True:
        speed_player = 6

    for i in lst_of_walls:
        if robot.rect.colliderect(i.rect):
            if robot.rect.centerx < i.rect.centerx:
                deepX = i.rect.left - robot.rect.right
            else:
                deepX = -(robot.rect.left - i.rect.right)
            if robot.rect.centery < i.rect.centery:
                deepY = i.rect.top - robot.rect.bottom
            else:
                deepY = -(robot.rect.top - i.rect.bottom)
            print(deepX, deepY)
            if abs(deepX) < abs(deepY):
                robot.rect.x += deepX
            else:
                robot.rect.y += deepY
            if (deepX == 6 and deepY == 6 or deepX == 6 and deepY == -19) or (deepX == -6 and deepY == 6 or deepX == -6 and deepY == -19):
                if flUp and flLeft or flUp and flRight:
                    robot.rect.y -= 6

    if pygame.mouse.get_pos()[0] - robot.rect.centerx > 0 and player_direction_left:
        robot.image = pygame.transform.flip(robot.image, True, False)
        pistol.image = pygame.transform.flip(pistol.image, True, False)
        pistolR.image = pygame.transform.flip(pistolR.image, True, False)
        player_direction_left = False
        player_direction_right = True
    if pygame.mouse.get_pos()[0] - robot.rect.centerx < 0 and player_direction_right:
        robot.image = pygame.transform.flip(robot.image, True, False)
        pistol.image = pygame.transform.flip(pistol.image, True, False)
        pistolR.image = pygame.transform.flip(pistolR.image, True, False)
        player_direction_right = False
        player_direction_left = True


    sc.fill((0, 0, 0))
    # rooms.fill((0, 0, 0))
    sc.blit(floor, C_floor)
    sc.blit(rooms, [C_rooms[0], C_rooms[1]-10])
    sc.blit(robot.image, (robot.rect.x-10, robot.rect.y - 20))
    pistol.update(pygame.mouse.get_pos())
    pistolR.update(pygame.mouse.get_pos())
    if pygame.mouse.get_pos()[0] - robot.rect.centerx > 0:
        pistol.rect.centerx = robot.rect.centerx
        pistol.rect.centery = robot.rect.centery
        sc.blit(pistol.image, pistol.rect)
    if pygame.mouse.get_pos()[0] - robot.rect.centerx < 0:
        pistolR.rect.centerx = robot.rect.centerx
        pistolR.rect.centery = robot.rect.centery
        sc.blit(pistolR.image, pistolR.rect)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()