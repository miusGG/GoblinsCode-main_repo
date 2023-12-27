import pygame as pg
from settings import set as s
from settings import load
from event import event, mobsAI
from draw import draw

pg.init()

#Устанавливаем параметры экрана и название окна
sc = pg.display.set_mode((s["DISPLAY"][0], s["DISPLAY"][1]))
pg.display.set_caption(s["WINNAME"])

clock = pg.time.Clock()
s["FPS"] = clock

#Подгрузкка всех текстур
load()


#Главная функция, запуск всех процессов
def main_menu():
    running = True
    while running:
        event(clock.get_fps())
        mobsAI()
        draw(sc, clock.get_fps())
        clock.tick(60)


main_menu()