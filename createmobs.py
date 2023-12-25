from settings import set as s
from mob import mob
from mob import mobs

def frog(mob):
    if (mob.pos[0] < s["player"]["posx"]):
        mob.pos[0] += 1 / s["FPS"].get_fps()
    else:
        mob.pos[0] -= 1 / s["FPS"].get_fps()
    if (mob.pos[1] < s["player"]["posy"]):
        mob.pos[1] += 1 / s["FPS"].get_fps()
    else:
        mob.pos[1] -= 1 / s["FPS"].get_fps()

mobs.append(mob("frog", (10, 10), 10, None, lambda : frog(mobs[len(mobs) - 1])))