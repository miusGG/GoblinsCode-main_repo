import math

from settings import set as s
from mob import Mob
from mob import mobs


#Создания ИИ мобов.
def frog(mob):
    if mob.pos[0] < s['player']['posx']:
        mob.pos[0] += 1 / s["FPS"].get_fps()
    else:
        mob.pos[0] -= 1 / s["FPS"].get_fps()
    if mob.pos[1] < s['player']['posy']:
        mob.pos[1] += 1 / s["FPS"].get_fps()
    else:
        mob.pos[1] -= 1 / s["FPS"].get_fps()


def slime(mob):
    speed = 100 / s["FPS"].get_fps()
    dx = s['player']['posx'] - mob.pos[0]
    dy = s['player']['posy'] - mob.pos[1]
    distance = math.hypot(dx, dy)
    vel_x = dx / distance * speed
    vel_y = dy / distance * speed
    while distance > speed:
        mob.pos[0] += vel_x
        mob.pos[1] += vel_y
        distance = math.hypot(s['player']['posx'] - mob.pos[0], s['player']['posy'] - mob.pos[1])


# Добавление мобов
mobs.append(Mob("bleb", (10, 10), 10, None, lambda : slime(mobs[len(mobs) - 1])))
#mobs.append(Mob("frog", (10, 10), 10, None, lambda : frog(mobs[len(mobs) - 1])))