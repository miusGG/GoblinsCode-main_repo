from generate import world, world_second_layer, fug_map, gen, doors2
from generate import collisions as col
import pygame as pg
from createmobs import spawn
from settings import set

count = 0


# Создания ИИ мобов.
def frog(mob):
    mob_pos_x = mob.pos[0]
    mob_pos_y = mob.pos[1]
    player_pos_x = set['player']['posx']
    player_pos_y = set['player']['posy']

    player_rect = pg.Rect(player_pos_x, player_pos_y, 1, 1)
    mob_rect = pg.Rect(mob_pos_x, mob_pos_y, 1, 1)

    if check_collision(player_rect, mob_rect):
        set["entity_damage_triggers"]["bleb_options"]["bleb-trigger"] = True

    if mob.pos[0] < set['player']['posx']:
        mob.pos[0] += 1 / set["FPS"].get_fps()
    else:
        mob.pos[0] -= 1 / set["FPS"].get_fps()
    if mob.pos[1] < set['player']['posy']:
        mob.pos[1] += 1 / set["FPS"].get_fps()
    else:
        mob.pos[1] -= 1 / set["FPS"].get_fps()


# Отрисовка 3 слоев игры.
def drawImgs(x, y, keyx, keyy, sc):
    # Сама карта
    if (keyx in world) and (keyy in world[keyx]):
        ceil = world[keyx][keyy]
        img = pg.transform.rotate(
            pg.transform.scale(set["textures"]["structures"][ceil[0]], (set["ceilSize"], set["ceilSize"])), ceil[1])
        sc.blit(img, (x, y))
    # Все с чем можно взаимодействовать
    if (keyx in world_second_layer) and (keyy in world_second_layer[keyx]):
        ceil = world_second_layer[keyx][keyy]
        img = pg.transform.rotate(
            pg.transform.scale(set["textures"]["secondLayer"][ceil[0]], (set["ceilSize"], set["ceilSize"])), ceil[1])
        sc.blit(img, (x, y))
    # Туман
    if (keyx in fug_map) and (keyy in fug_map[keyx]):
        ceil = fug_map[keyx][keyy]
        img = pg.transform.rotate(
            pg.transform.scale(set["textures"]["structures"][ceil[0]], (set["ceilSize"], set["ceilSize"])), ceil[1])
        sc.blit(img, (x, y))


# Функция анимации игрока
def playAnimation(animation, time):
    global count
    if not set["ONPAUSE"]:
        count += 1
    if count == time:
        count = 0
    cframes = len(set["textures"]["animations"][animation])
    return set["textures"]["animations"][animation][int(count // (time / cframes))]


# Проверка будующего место положения игрока на то, может ли он там находиться по ИКС
def checkCollisionx(x):
    for i in range(len(col)):
        if ((x + 1 > col[i][0][0]) and (x < col[i][0][0] + col[i][0][2])) and (
                (set["player"]["posy"] + 1 > col[i][0][1]) and set["player"]["posy"] < col[i][0][1] + col[i][0][3]):
            if col[i][1] == "stop":
                return False
            elif col[i][1] == "generate":
                gen.generateRoom((col[i][2][0][0] + doors2[col[i][2][1]][0], col[i][2][0][1] + doors2[col[i][2][1]][1]),
                                 [2, 1], col[i][2][1])
                spawn(1, (col[i][2][0][0] + doors2[col[i][2][1]][0], col[i][2][0][1] + doors2[col[i][2][1]][1]), frog)
                del (col[i])
                break
    return True


# ... по ИГРЕК
def checkCollisiony(y):
    for i in range(len(col)):
        if ((y + 1 > col[i][0][1]) and (y < col[i][0][1] + col[i][0][3])) and (
                (set["player"]["posx"] + 1 > col[i][0][0]) and set["player"]["posx"] < col[i][0][0] + col[i][0][2]):
            if col[i][1] == "stop":
                return False
            elif col[i][1] == "generate":
                gen.generateRoom((col[i][2][0][0] + doors2[col[i][2][1]][0], col[i][2][0][1] + doors2[col[i][2][1]][1]),
                                 [2, 1], col[i][2][1])
                spawn(1, (col[i][2][0][0] + doors2[col[i][2][1]][0], col[i][2][0][1] + doors2[col[i][2][1]][1]), frog)
                del (col[i])
                break
    return True


# Проверка коллизий для игрока и моба
def check_collision(player_rect, mob_rect):
    if player_rect.colliderect(mob_rect):
        return True
    else:
        pass
