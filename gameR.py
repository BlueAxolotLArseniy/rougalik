import pygame
import math
import random

pygame.init()

sc = pygame.display.set_mode((800, 500), pygame.RESIZABLE)
pygame.display.set_icon(pygame.image.load("textures/others/gameicon.bmp"))
pygame.display.set_caption('GFR - Game For Rogalick')

XpointX = 20
YpointY = 20

FPS_SECONDS = 0

number_of_on_mouse = 0

SHOW_HITBOXES_ON_PLAYER = True
SHOW_HITBOXES = True

string_of_bullet = f'test_bullet{number_of_on_mouse} = Bullet(0, 0, "textures/gun/bullet/yellow/rectangle.png")'
name_of_bullet = f'test_bullet{number_of_on_mouse}'

list_of_bullets = []
copy_list_of_bullets = list_of_bullets

pygame.mouse.set_visible(False)

player_direction_right = True
player_direction_left = False

speed_player = 6

cursor = pygame.image.load('textures/others/cursor.png').convert()
cursor.set_colorkey((0, 0, 0))
cursor = pygame.transform.scale(cursor, (cursor.get_width() * 2, cursor.get_height() * 2))

coordinates1 = None
coordinates2 = None

FPS = 40
list_for_squares = []

file = open('settings/samples/usual_fightes.txt', 'r')

file2 = open('settings/samples/usual_fightes_rooms.txt', 'r')


matrix_of_rooms = [[w for w in line.replace('\n', '')] for line in file]
print(matrix_of_rooms)

matrix_of_rooms_settings = [[w for w in line.replace('\n', '')] for line in file2]

lst_of_walls = []

class Bullet(pygame.sprite.Sprite):

    printing = False
    speed = 10

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

    def new_coordinates(self):

        # Получаем координаты мыши относительно экрана
        mouse_pos = pygame.mouse.get_pos()

        # Вычисляем координаты мыши относительно центра экрана
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        # Вычисляем направление
        angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)
        dx = math.cos(angle)
        dy = math.sin(angle)
        self.direction = (dx, dy)

    def move(self):
        # перемещаем атаку
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

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

rooms = pygame.Surface((5000, 5000), pygame.SRCALPHA, 32)
C_rooms = rooms.get_rect()
C_rooms.x = 0
C_rooms.y = 0
rooms = rooms.convert_alpha()

pistol = Gun(0, 0, 'textures/gun/pistol/p250.png')
pistolR = Gun(0, 0, 'textures/gun/pistol/p250R.png')

test_bullet = Bullet(0, 0, 'textures/gun/bullet/yellow/rectangle.png')

floor = pygame.Surface((5000, 5000), pygame.SRCALPHA, 32)
C_floor = floor.get_rect()
C_floor.x = 0
C_floor.y = 0
floor = floor.convert_alpha()

robot = Hero(400, 250, 'textures/heroes/robot/red_robot.png')

def draw_all_in_all():
    global matrix_of_rooms, XpointX, YpointY, spawnpoint
    points = 0
    for i in range(len(matrix_of_rooms)):
        for p in range(len(matrix_of_rooms[i])):
            if XpointX == 1320: XpointX = 20
            k = matrix_of_rooms_settings[i][p]
            kSETTINGS = matrix_of_rooms[i][p]
            if k == '0' or k == '7':
                q = open('settings/rooms&locations/vode/vode.txt')
                q = [[w for w in line.replace('\n', '')] for line in q]
                print(q)
                dr_all(q)
            elif k == '-':
                q = open('settings/rooms&locations/hall/horizontal_hall.txt')
                q = [[w for w in line.replace('\n', '')] for line in q]
                dr_all(q)
            elif k == '|':
                q = open('settings/rooms&locations/hall/vertical_hall.txt')
                q = [[w for w in line.replace('\n', '')] for line in q]
                dr_all(q)
            elif k == 'v':
                pass
            elif kSETTINGS == '4':
                spawnpoint = [XpointX + 110, YpointY + 110]
            else:
                if k == 'A':
                    q = open('settings/rooms&locations/fight/ROOM_A.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'B':
                    q = open('settings/rooms&locations/fight/ROOM_B.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'C':
                    q = open('settings/rooms&locations/fight/ROOM_C.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'D':
                    q = open('settings/rooms&locations/fight/ROOM_D.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'E':
                    q = open('settings/rooms&locations/fight/ROOM_E.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'F':
                    q = open('settings/rooms&locations/fight/ROOM_F.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'G':
                    q = open('settings/rooms&locations/fight/ROOM_G.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'H':
                    q = open('settings/rooms&locations/fight/ROOM_H.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'I':
                    q = open('settings/rooms&locations/fight/ROOM_I.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'J':
                    q = open('settings/rooms&locations/fight/ROOM_J.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'K':
                    q = open('settings/rooms&locations/fight/ROOM_K.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'L':
                    q = open('settings/rooms&locations/fight/ROOM_L.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'M':
                    q = open('settings/rooms&locations/fight/ROOM_M.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'N':
                    q = open('settings/rooms&locations/fight/ROOM_N.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
                elif k == 'O':
                    q = open('settings/rooms&locations/fight/ROOM_O.txt')
                    q = [[w for w in line.replace('\n', '')] for line in q]
                    dr_all(q)
            XpointX += 260
            print('комната')

        YpointY += 260
        print('система комнат', points)
        points += 1

def new_bullet():
    global number_of_on_mouse, string_of_bullet, list_of_bullets, name_of_bullet
    number_of_on_mouse = len(list_of_bullets)
    list_of_bullets.append(Bullet(robot.rect.centerx, robot.rect.centery, 'textures/gun/bullet/yellow/rectangle.png'))
    list_of_bullets[number_of_on_mouse].printing = True
    list_of_bullets[number_of_on_mouse].rect.center = robot.rect.center
    list_of_bullets[number_of_on_mouse].new_coordinates()
    rotate(list_of_bullets[number_of_on_mouse])



def rotate(self):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rel_x, rel_y = mouse_x - self.rect.x, mouse_y - self.rect.y
    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    self.image = pygame.transform.rotate(self.original_image, int(angle))
    self.rect = self.image.get_rect(center=self.rect.center)

def dr_all(file):
    global YpointY
    point = 0
    ok = YpointY
    for y in range(13):
        dr_one_stack(point, ok, file)
        point += 1
        ok+=20

def dr_one_stack(x, y, file):
    global sc, pointQ, yQ, XpointX
    point = XpointX
    print(len(matrix_of_rooms), x)
    for i in file[x]:
        if i == '1':
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
        if i == '0':
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
draw_all_in_all()
C_rooms.x -= 260
C_rooms.y -= 500
C_floor.x -= 260
C_floor.y -= 500
for i in lst_of_walls:
    i.rect.y -= 500
    i.rect.x -= 260
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
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            new_bullet()

    mouse_pos = pygame.mouse.get_pos()


    if flDown == True:
        C_rooms.y -= speed_player
        C_floor.y -= speed_player
        for i in lst_of_walls:
            i.rect.y -= speed_player
        for i in list_of_bullets:
            i.rect.y -= speed_player
    if flUp == True:
        C_rooms.y += speed_player
        C_floor.y += speed_player
        for i in lst_of_walls:
            i.rect.y += speed_player
        for i in list_of_bullets:
            i.rect.y += speed_player
    if flLeft == True:
        C_rooms.x += speed_player
        C_floor.x += speed_player
        for i in lst_of_walls:
            i.rect.x += speed_player
        for i in list_of_bullets:
            i.rect.x += speed_player
    if flRight == True:
        C_rooms.x -= speed_player
        C_floor.x -= speed_player
        for i in lst_of_walls:
            i.rect.x -= speed_player
        for i in list_of_bullets:
            i.rect.x -= speed_player
    if flShift == True:
        speed_player = 2
    if flShift != True:
        speed_player = 6

    for i in lst_of_walls:
        if robot.rect.colliderect(i.rect):
            # print('awd')
            if robot.rect.centerx < i.rect.centerx:
                deepX = i.rect.left - robot.rect.right
            else:
                deepX = -(robot.rect.left - i.rect.right)
            if robot.rect.centery < i.rect.centery:
                deepY = i.rect.top - robot.rect.bottom
            else:
                deepY = -(robot.rect.top - i.rect.bottom)
            # print(deepX, deepY)
            if abs(deepX) < abs(deepY):
                C_rooms.x -= deepX
                C_floor.x -= deepX
                for i in lst_of_walls:
                    i.rect.x -= deepX
            else:
                C_rooms.y -= deepY
                C_floor.y -= deepY
                for i in lst_of_walls:
                    i.rect.y -= deepY
            if (deepX == 6 and deepY == 6 or deepX == 6 and deepY == -19) or (deepX == -6 and deepY == 6 or deepX == -6 and deepY == -19):
                if flUp and flLeft or flUp and flRight:
                    C_rooms.y += 6
                    C_floor.y += 6
                    for i in lst_of_walls:
                        i.rect.y += 6
        for i2 in list_of_bullets:
            if i2.rect.colliderect(i.rect):
                i2.printing = False

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

    copy_list_of_bullets = list_of_bullets
    sc.fill((0, 0, 0))
    # rooms.fill((0, 0, 0))
    sc.blit(floor, C_floor)
    sc.blit(rooms, [C_rooms[0], C_rooms[1]-10])
    sc.blit(robot.image, (robot.rect.x-10, robot.rect.y - 20))
    for i in list_of_bullets:
        if i.printing == True:
            sc.blit(i.image, i.rect)
            i.move()
        else:
            copy_list_of_bullets.remove(i)
            list_of_bullets = copy_list_of_bullets
    if pygame.mouse.get_pos()[0] - robot.rect.centerx > 0:
        pistol.rect.centerx = robot.rect.centerx
        pistol.rect.centery = robot.rect.centery
        rotate(pistol)
        sc.blit(pistol.image, pistol.rect)
    elif pygame.mouse.get_pos()[0] - robot.rect.centerx < 0:
        pistolR.rect.centerx = robot.rect.centerx
        pistolR.rect.centery = robot.rect.centery
        rotate(pistolR)
        sc.blit(pistolR.image, pistolR.rect)
    sc.blit(cursor, (pygame.mouse.get_pos()[0]-10, pygame.mouse.get_pos()[1]-10))
    if SHOW_HITBOXES_ON_PLAYER:
        pygame.draw.rect(sc, (255, 255, 255), (robot.rect.x, robot.rect.y, 20, 20), 3)
    if SHOW_HITBOXES:
        for i in lst_of_walls:
            pygame.draw.rect(sc, (255, 128, 0), (i.rect.x, i.rect.y, 20, 20), 1)
    pygame.display.flip()
    clock.tick(FPS)
    # print(number_of_on_mouse, robot.rect.center)
    FPS_SECONDS += 1
    print(FPS_SECONDS, FPS)


pygame.quit()