import sys
from generate import world, world_second_layer, fug_map, gen, doors2
from generate import collisions as col
import pygame as pg

from settings import set as s

debug_prefix = "[MF]"
count = 0

def drawImgs(x, y, keyx, keyy, sc):
    if (keyx in world) and (keyy in world[keyx]):
        ceil = world[keyx][keyy]
        img = pg.transform.rotate(pg.transform.scale(s["textures"]["structures"][ceil[0]], (s["ceilSize"], s["ceilSize"])), ceil[1])
        sc.blit(img, (x, y))
    if (keyx in world_second_layer) and (keyy in world_second_layer[keyx]):
        ceil = world_second_layer[keyx][keyy]
        img = pg.transform.rotate(pg.transform.scale(s["textures"]["secondLayer"][ceil[0]], (s["ceilSize"], s["ceilSize"])), ceil[1])
        sc.blit(img, (x, y))
    if (keyx in fug_map) and (keyy in fug_map[keyx]):
        ceil = fug_map[keyx][keyy]
        img = pg.transform.rotate(pg.transform.scale(s["textures"]["structures"][ceil[0]], (s["ceilSize"], s["ceilSize"])), ceil[1])
        sc.blit(img, (x, y))


def playAnimation(animation, time):
    global count
    if not s["ONPAUSE"]:
        count += 1
    if count == time:
        count = 0
    cframes = len(s["textures"]["animations"][animation])
    return s["textures"]["animations"][animation][int(count//(time/cframes))]

def checkCollisionx(x):
    for i in range(len(col)):
        if ((x + 1> col[i][0][0]) and (x < col[i][0][0] + col[i][0][2])) and ((s["player"]["posy"] + 1 > col[i][0][1]) and s["player"]["posy"] < col[i][0][1] + col[i][0][3]):
            if (col[i][1] == "stop"):
                return False
            elif (col[i][1] == "generate"):
                gen.generateRoom((col[i][2][0][0] + doors2[col[i][2][1]][0], col[i][2][0][1] + doors2[col[i][2][1]][1]), [2, 1], col[i][2][1])
                del(col[i])
                break
    return True

def checkCollisiony(y):
    for i in range(len(col)):
        if ((y + 1> col[i][0][1]) and (y < col[i][0][1] + col[i][0][3])) and ((s["player"]["posx"] + 1> col[i][0][0]) and s["player"]["posx"] < col[i][0][0] + col[i][0][2]):
            if (col[i][1] == "stop"):
                return False
            elif (col[i][1] == "generate"):
                gen.generateRoom((col[i][2][0][0] + doors2[col[i][2][1]][0], col[i][2][0][1] + doors2[col[i][2][1]][1]), [2, 1], col[i][2][1])
                del(col[i])
                break
    return True

def debug(text):
    global debug_prefix
    print(debug_prefix + " " + text)

def exit():
    debug("Stoping")
    debug("Good Bye!")
    sys.exit(0)