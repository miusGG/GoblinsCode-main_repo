import pygame as pg
from settings import set
from settings import load
from event import event, mobsAI
from draw import draw

pg.init()

# Устанавливаем параметры экрана и название окна.
sc = pg.display.set_mode((set["DISPLAY"][0], set["DISPLAY"][1]))
pg.display.set_caption(set["WINNAME"])

# Тип инвента для получения урона
DAMAGEEVENT, timer = pg.USEREVENT + 1, 3000
pg.time.set_timer(DAMAGEEVENT, timer)

clock = pg.time.Clock()
set["FPS"] = clock

# Подгрузкка всех текстур
load()


# Главная функция, запуск всех процессов
def main_menu():
    running = True
    while running:
        event(clock.get_fps())
        mobsAI()
        draw(sc, clock.get_fps())
        clock.tick(60)


main_menu()
