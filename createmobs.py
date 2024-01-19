from mob import Mob
from mob import mobs
from settings import set as s


# Прототип нового моба
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
roomsize = s["roomSize"] * 2 + 6


def spawn(type, c, AI):
    if type == 1:
        x = 0
        y = 0
        mobs.append(Mob("slime", (x + c[0] * roomsize, y + c[1] * roomsize), 10, None, lambda: AI(mobs[len(mobs) - 1])))
