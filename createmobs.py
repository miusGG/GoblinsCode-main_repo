import math

from mob import Mob
from mob import mobs
from mob import MobNow
import pygame
import time
import threading
from funcs import check_collision
from settings import set as s


#Создания ИИ мобов.
def frog(mob):
    mob_pos_x = mob.pos[0]
    mob_pos_y = mob.pos[1]
    player_pos_x = s['player']['posx']
    player_pos_y = s['player']['posy']

    player_rect = pygame.Rect(player_pos_x, player_pos_y, 1, 1)
    mob_rect = pygame.Rect(mob_pos_x, mob_pos_y, 1, 1)

    if check_collision(player_rect, mob_rect):
        s["entity_damage_triggers"]["bleb_options"]["bleb-trigger"] = True

    if mob.pos[0] < s['player']['posx']:
        mob.pos[0] += 1 / s["FPS"].get_fps()
    else:
        mob.pos[0] -= 1 / s["FPS"].get_fps()
    if mob.pos[1] < s['player']['posy']:
        mob.pos[1] += 1 / s["FPS"].get_fps()
    else:
        mob.pos[1] -= 1 / s["FPS"].get_fps()


#Прототип нового моба
def glider(mob):

    if mob.pos[0] < s['player']['posx']:
        mob.pos[0] += 1 / s["FPS"].get_fps()
    else:
        mob.pos[0] -= 1 / s["FPS"].get_fps()
    if mob.pos[1] < s['player']['posy']:
        mob.pos[1] += 1 / s["FPS"].get_fps()
    else:
        mob.pos[1] -= 1 / s["FPS"].get_fps()


# Добавление мобов
mobs.append(Mob("slime", (10, 10), 10, None, lambda: frog(mobs[len(mobs) - 1])))