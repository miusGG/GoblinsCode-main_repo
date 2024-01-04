import pygame as pg
import time

from settings import set as s
from settings import buttons, buttonsSettings, ingamebuttons, buttonVideoSettings
from generate import world, collisions, world_map
from funcs import playAnimation, drawImgs
from mob import mobs

pg.font.init()
font = pg.font.SysFont('arial', 30)
font2 = pg.font.SysFont('arial', 45)

#Функция отрисовки всех функций.
def draw(sc, fps):
    if s["INGAME"]:
        draw_game(sc, fps)
    elif s["INMENU"]:
        s["player"]["posy"] = 0
        s["player"]["posx"] = 0
        draw_menu(sc)
    elif s["INSETTINGS"]:
        draw_settings(sc)
    elif s["INVIDEOSETTINGS"]:
        draw_video_settings(sc)
    elif s["deth"]:
        draw_deth(sc)


#Функция отрисовки паузы
def draw_onpause(sc):
    ingamebuttons["exit_from_game"].check_hover(pg.mouse.get_pos())
    ingamebuttons["exit_from_game"].draw(sc)


#Прорисовка смерти
def draw_deth(sc):
    s["INGAME"] = False
    s["ONPAUSE"] = False
    s["INMENU"] = True
    sc.fill((0, 0, 0))

    WIDTH, HEIGHT = s["DISPLAY"]

    text = font.render('YOU ARE DIE!', True, (255, 255, 255))

    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    sc.blit(text, text_rect)

    ingamebuttons["exit_from_game"].check_hover(pg.mouse.get_pos())
    ingamebuttons["exit_from_game"].draw(sc)

    pg.display.flip()


#Функиця открисовки настроек
def draw_settings(sc):
    sc.fill((41, 39, 41))
    # sc.blit(pg.transform.scale(s["textures"]["gui"]["settingsPicture"], s["DISPLAY"]), (0, 0))
    buttonsSettings["exit_from_settings"].check_hover(pg.mouse.get_pos())
    buttonsSettings["exit_from_settings"].draw(sc)
    buttonsSettings["video_set"].check_hover(pg.mouse.get_pos())
    buttonsSettings["video_set"].draw(sc)
    buttonsSettings["volme_set"].check_hover(pg.mouse.get_pos())
    buttonsSettings["volme_set"].draw(sc)
    buttonsSettings["keys_set"].check_hover(pg.mouse.get_pos())
    buttonsSettings["keys_set"].draw(sc)
    pg.display.flip()


#Функция отрисовки видео-настроек
def draw_video_settings(sc):
    sc.fill((41, 39, 41))
    # sc.blit(pg.transform.scale(s["textures"]["gui"]["settingsPicture"], s["DISPLAY"]), (0, 0))
    buttonVideoSettings["hightVideo"].check_hover(pg.mouse.get_pos())
    buttonVideoSettings["hightVideo"].draw(sc)
    buttonVideoSettings["lowVideo"].check_hover(pg.mouse.get_pos())
    buttonVideoSettings["lowVideo"].draw(sc)
    buttonVideoSettings["mediumVideo"].check_hover(pg.mouse.get_pos())
    buttonVideoSettings["mediumVideo"].draw(sc)
    buttonVideoSettings["exit_from_video_settings"].check_hover(pg.mouse.get_pos())
    buttonVideoSettings["exit_from_video_settings"].draw(sc)
    pg.display.flip()


#Функция отрисовки главного меню
def draw_menu(sc):
    sc.blit(pg.transform.scale(s["textures"]["gui"]["mainPicture"], s["DISPLAY"]), (0, 0))
    # Создание кнопки - "Начать игру"
    WIDTH, HEIGHT = s["DISPLAY"]
    font = pg.font.Font(None, 104)
    # text_surface = font.render("Goblins Gold!", True, (255, 255, 255))
    # text_rect = text_surface.get_rect(center=(WIDTH / 2 - (104 / 2) + 30 + 20 + 10 + 10 + 10, 70))
    # sc.blit(text_surface, text_rect)

    # Выводим кнопки
    buttons["settings"].check_hover(pg.mouse.get_pos())
    buttons["settings"].draw(sc)
    buttons["exit"].check_hover(pg.mouse.get_pos())
    buttons["exit"].draw(sc)
    buttons["start"].check_hover(pg.mouse.get_pos())
    buttons["start"].draw(sc)
    pg.display.flip()


#Функция отрисовки ИГРЫ
def draw_game(sc, fps):
    #Зливка экрана
    sc.fill((41, 39, 41))
    w, h = pg.display.get_surface().get_size()

    #Цикл на отрисовку клеток
    for i in range(0, int(w / 2) // s["ceilSize"] + 3):
        for j in range(0, int(h / 2) // s["ceilSize"] + 3):

            #Костыль системы.
            corectx = 1
            corecty = 1
            if (s["player"]['posx'] < 0):
                corectx = 0
            if (s["player"]['posy'] < 0):
                corecty = 0

            #Получаем координаты из КЛЕТОК в ПИКСЕЛЯХ
            x1 = w // 2 + i * s["ceilSize"] - (s["player"]['posx'] % 1) * s["ceilSize"] - s["ceilSize"] // 2
            y1 = h // 2 + j * s["ceilSize"] - (s["player"]['posy'] % 1) * s["ceilSize"] - s["ceilSize"] // 2
            keyx1 = str(int(s["player"]['posx']) + i - 1 + corectx)
            keyy1 = str(int(s["player"]['posy']) + j - 1 + corecty)

            x2 = w // 2 - i * s["ceilSize"] - (s["player"]['posx'] % 1) * s["ceilSize"] - s["ceilSize"] // 2
            y2 = h // 2 + j * s["ceilSize"] - (s["player"]['posy'] % 1) * s["ceilSize"] - s["ceilSize"] // 2
            keyx2 = str(int(s["player"]['posx']) - i - 1 + corectx)
            keyy2 = str(int(s["player"]['posy']) + j - 1 + corecty)

            x3 = w // 2 - i * s["ceilSize"] - (s["player"]['posx'] % 1) * s["ceilSize"] - s["ceilSize"] // 2
            y3 = h // 2 - j * s["ceilSize"] - (s["player"]['posy'] % 1) * s["ceilSize"] - s["ceilSize"] // 2
            keyx3 = str(int(s["player"]['posx']) - i - 1 + corectx)
            keyy3 = str(int(s["player"]['posy']) - j - 1 + corecty)

            x4 = w // 2 + i * s["ceilSize"] - (s["player"]['posx'] % 1) * s["ceilSize"] - s["ceilSize"] // 2
            y4 = h // 2 - j * s["ceilSize"] - (s["player"]['posy'] % 1) * s["ceilSize"] - s["ceilSize"] // 2
            keyx4 = str(int(s["player"]['posx']) + i - 1 + corectx)
            keyy4 = str(int(s["player"]['posy']) - j - 1 + corecty)

            #Рисуем все клеточки на каждой части экрана
            drawImgs(x1, y1, keyx1, keyy1, sc)
            drawImgs(x2, y2, keyx2, keyy2, sc)
            drawImgs(x3, y3, keyx3, keyy3, sc)
            drawImgs(x4, y4, keyx4, keyy4, sc)

    #Отображение колизий на f1
    if s["showCollisions"]:
        #Создание колизии для игрока
        x = w // 2 - s["ceilSize"] // 2
        y = h // 2 - s["ceilSize"] // 2
        pg.draw.circle(sc, (255, 255, 255), (x, y), 5)
        pg.draw.rect(sc, (255, 255, 255),
                     (w / 2 - s["ceilSize"] / 2, h / 2 - s["ceilSize"] / 2, s["ceilSize"], s["ceilSize"]), 1)
        for i in collisions:
            x = w // 2 + i[0][0] * s["ceilSize"] - (s["player"]["posx"]) * s["ceilSize"] - s["ceilSize"] // 2
            y = h // 2 + i[0][1] * s["ceilSize"] - (s["player"]["posy"]) * s["ceilSize"] - s["ceilSize"] // 2
            w2 = i[0][2] * s["ceilSize"]
            h2 = i[0][3] * s["ceilSize"]
            #Колизии для стен
            if i[1] == "stop":
                color = (255, 0, 0)
            #Колизии для генерации новой комнаты
            elif i[1] == "generate":
                color = (0, 255, 0)
            pg.draw.circle(sc, color, (x, y), 5)
            pg.draw.rect(sc, color, (x, y, w2, h2), 1)
    #Отрисовка мобов
    for i in mobs:
        x = w // 2 + i.pos[0] * s["ceilSize"] - (s["player"]["posx"]) * s["ceilSize"] - s["ceilSize"] // 2
        y = h // 2 + i.pos[1] * s["ceilSize"] - (s["player"]["posy"]) * s["ceilSize"] - s["ceilSize"] // 2
        sc.blit(pg.transform.scale(s["textures"]["entity"][i.texture], (s["ceilSize"], s["ceilSize"])), (x, y))

    #Отрисовка игрока
    if (s["player"]["speedx"] != 0) or (s["player"]["speedy"] != 0):
        sc.blit(pg.transform.flip(pg.transform.scale(playAnimation("player", 30), (s["ceilSize"], s["ceilSize"])),
                                  s["player"]["rotate"], False), (w / 2 - s["ceilSize"] / 2, h / 2 - s["ceilSize"] / 2))
    else:
        sc.blit(pg.transform.flip(pg.transform.scale(s["player"]["texture"], (s["ceilSize"], s["ceilSize"])),
                                  s["player"]["rotate"], False), (w / 2 - s["ceilSize"] / 2, h / 2 - s["ceilSize"] / 2))

    # health bar
    pg.draw.rect(sc, (255, 204, 204), (100, 930, 300, 30))
    pg.draw.rect(sc, (255, 51, 51), (100, 930, (300 / 100) * s["player"]['health'], 30))

    #Координаты и ФПС
    img1 = font.render("X:" + str(int(s["player"]['posx'])) + " Y:" + str(int(s["player"]['posy'])), True, (0, 0, 0))
    img2 = font.render("FPS:" + str(int(fps)), True, (0, 0, 0))
    sc.blit(img1, (100, 360))
    sc.blit(img2, (100, 390))

    #ОТрисовка миникарты
    draw_minimap(sc)

    #Отрисовка паузы
    if s["ONPAUSE"]:
        draw_onpause(sc)

    #Обновление экрана
    pg.display.flip()


#Функция открисовки миникарты
def draw_minimap(sc):
    pg.draw.rect(sc, (40, 40, 40),
                 (s["MINIMAP"][0] - 5, s["MINIMAP"][0] - 5, s["MINIMAP"][1] + 10, s["MINIMAP"][1] + 10))
    pg.draw.rect(sc, (80, 80, 80), (s["MINIMAP"][0], s["MINIMAP"][0], s["MINIMAP"][1], s["MINIMAP"][1]))

    for i in world_map:
        for j in world_map[i]:
            # Координаты и размеры комнаты на миникарте (создание самих комнат)
            coord = [
                [
                    int(i) * (s["MINIMAP"][2]) + s["MINIMAP"][1] // 2 - (s["player"]["posx"]) * (
                            s["MINIMAP"][2] / (s["roomSize"] * 2 + 6)) - 4 + 12.5,
                    int(j) * (s["MINIMAP"][2]) + s["MINIMAP"][1] // 2 - (s["player"]["posy"]) * (
                            s["MINIMAP"][2] / (s["roomSize"] * 2 + 6)) - 4 + 12.5,
                    s["MINIMAP"][2] - 25,
                    s["MINIMAP"][2] - 25
                ],
                [
                    int(i) * (s["MINIMAP"][2]) + s["MINIMAP"][1] // 2 - (s["player"]["posx"]) * (
                            s["MINIMAP"][2] / (s["roomSize"] * 2 + 6)) - 4,
                    int(j) * (s["MINIMAP"][2]) + s["MINIMAP"][1] // 2 - (s["player"]["posy"]) * (
                            s["MINIMAP"][2] / (s["roomSize"] * 2 + 6)) - 4 + 6.25 + (s["MINIMAP"][2] - 25) // 2,
                    s["MINIMAP"][2],
                    12.5
                ],
                [
                    int(i) * (s["MINIMAP"][2]) + s["MINIMAP"][1] // 2 - (s["player"]["posx"]) * (
                            s["MINIMAP"][2] / (s["roomSize"] * 2 + 6)) - 4 + 6.25 + (s["MINIMAP"][2] - 25) // 2,
                    int(j) * (s["MINIMAP"][2]) + s["MINIMAP"][1] // 2 - (s["player"]["posy"]) * (
                            s["MINIMAP"][2] / (s["roomSize"] * 2 + 6)) - 4,
                    12.5,
                    s["MINIMAP"][2]
                ]
            ]

            # Убрием лишние проходы на миникарте
            if (0 not in world_map[i][j][2]):
                coord[2][3] -= 13
                coord[2][1] += 13
            if (1 not in world_map[i][j][2]):
                coord[2][3] -= 13
            if (2 not in world_map[i][j][2]):
                coord[1][2] -= 13
            if (3 not in world_map[i][j][2]):
                coord[1][2] -= 13
                coord[1][0] += 13

            # Цикл чтобы комнаты не вылезали за миникарту
            for d in coord:
                if (d[0] >= s["MINIMAP"][1] + s["MINIMAP"][0]):
                    d[0] = s["MINIMAP"][1] + s["MINIMAP"][0]
                    d[2] = 0
                    d[3] = 0
                elif (d[0] + d[2] >= s["MINIMAP"][1] + s["MINIMAP"][0]):
                    d[2] = s["MINIMAP"][1] + s["MINIMAP"][0] - d[0] + 1

                if (d[0] <= s["MINIMAP"][0]):
                    d[2] -= abs(d[0] - s["MINIMAP"][0])
                    d[0] = s["MINIMAP"][0]

                if (d[1] >= s["MINIMAP"][1] + s["MINIMAP"][0]):
                    d[1] = s["MINIMAP"][1] + s["MINIMAP"][0]
                    d[2] = 0
                    d[3] = 0
                elif (d[1] + d[3] >= s["MINIMAP"][1] + s["MINIMAP"][0]):
                    d[3] = s["MINIMAP"][1] + s["MINIMAP"][0] - d[1] + 1

                if (d[1] <= s["MINIMAP"][0]):
                    d[3] -= abs(d[1] - s["MINIMAP"][0])
                    d[1] = s["MINIMAP"][0]

            # Задаем цвет по типу команты
            if (world_map[i][j][1] == -1):
                color = (40, 40, 0)
            elif (world_map[i][j][1] == 0):
                color = (40, 0, 0)
            else:
                color = (40, 40, 40)

            # Отрисовка квадрата команты и путей
            pg.draw.rect(sc, color, (coord[1][0], coord[1][1], coord[1][2], coord[1][3]))
            pg.draw.rect(sc, color, (coord[2][0], coord[2][1], coord[2][2], coord[2][3]))
            pg.draw.rect(sc, color, (coord[0][0], coord[0][1], coord[0][2], coord[0][3]))
    # Отображение игрока (красная точка)
    pg.draw.circle(sc, (255, 0, 0), (s["MINIMAP"][0] + s["MINIMAP"][1] // 2, s["MINIMAP"][0] + s["MINIMAP"][1] // 2), 4)
