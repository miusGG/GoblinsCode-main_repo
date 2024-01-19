import pygame as pg
from settings import set
from settings import buttons, buttonsSettings, ingamebuttons, buttonVideoSettings, LastMenubButtons, DethMenubButtons
from generate import collisions, world_map
from funcs import playAnimation, drawImgs
from mob import mobs

pg.font.init()
font = pg.font.SysFont('arial', 30)
font2 = pg.font.SysFont('arial', 45)


# Функция отрисовки всех функций.
def draw(sc, fps):
    if set["INGAME"]:
        draw_game(sc, fps)
    elif set["INMENU"]:
        set["player"]["posy"] = 0
        set["player"]["posx"] = 0
        draw_menu(sc)
    elif set["INSETTINGS"]:
        draw_settings(sc)
    elif set["INVIDEOSETTINGS"]:
        draw_video_settings(sc)
    elif set["deth"]:
        set["player"]["posy"] = 0
        set["player"]["posx"] = 0
        draw_deth(sc)
    elif set["lastRoom"]:
        set["player"]["posy"] = 0
        set["player"]["posx"] = 0
        draw_lastmenu(sc)


# Функция отрисовки паузы
def draw_onpause(sc):
    ingamebuttons["exit_from_game"].check_hover(pg.mouse.get_pos())
    ingamebuttons["exit_from_game"].draw(sc)


def draw_lastmenu(sc):
    sc.fill((41, 39, 41))
    LastMenubButtons["exit_to_menu"].check_hover(pg.mouse.get_pos())
    LastMenubButtons["exit_to_menu"].draw(sc)
    LastMenubButtons["text"].check_hover(pg.mouse.get_pos())
    LastMenubButtons["text"].draw(sc)
    pg.display.flip()


# Прорисовка смерти
def draw_deth(sc):
    sc.fill((41, 39, 41))
    DethMenubButtons["exit_to_menu"].check_hover(pg.mouse.get_pos())
    DethMenubButtons["exit_to_menu"].draw(sc)
    DethMenubButtons["text"].check_hover(pg.mouse.get_pos())
    DethMenubButtons["text"].draw(sc)
    pg.display.flip()


# Функиця открисовки настроек
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


# Функция отрисовки видео-настроек
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


# Функция отрисовки главного меню
def draw_menu(sc):
    sc.blit(pg.transform.scale(set["textures"]["gui"]["mainPicture"], set["DISPLAY"]), (0, 0))

    # Выводим кнопки
    buttons["settings"].check_hover(pg.mouse.get_pos())
    buttons["settings"].draw(sc)
    buttons["exit"].check_hover(pg.mouse.get_pos())
    buttons["exit"].draw(sc)
    buttons["start"].check_hover(pg.mouse.get_pos())
    buttons["start"].draw(sc)
    pg.display.flip()


# Функция отрисовки ИГРЫ
def draw_game(sc, fps):
    # Зливка экрана
    sc.fill((41, 39, 41))
    w, h = pg.display.get_surface().get_size()

    # Цикл на отрисовку клеток
    for i in range(0, int(w / 2) // set["ceilSize"] + 3):
        for j in range(0, int(h / 2) // set["ceilSize"] + 3):

            # Костыль системы.
            corectx = 1
            corecty = 1
            if (set["player"]['posx'] < 0):
                corectx = 0
            if (set["player"]['posy'] < 0):
                corecty = 0

            # Получаем координаты из КЛЕТОК в ПИКСЕЛЯХ
            x1 = w // 2 + i * set["ceilSize"] - (set["player"]['posx'] % 1) * set["ceilSize"] - set["ceilSize"] // 2
            y1 = h // 2 + j * set["ceilSize"] - (set["player"]['posy'] % 1) * set["ceilSize"] - set["ceilSize"] // 2
            keyx1 = str(int(set["player"]['posx']) + i - 1 + corectx)
            keyy1 = str(int(set["player"]['posy']) + j - 1 + corecty)

            x2 = w // 2 - i * set["ceilSize"] - (set["player"]['posx'] % 1) * set["ceilSize"] - set["ceilSize"] // 2
            y2 = h // 2 + j * set["ceilSize"] - (set["player"]['posy'] % 1) * set["ceilSize"] - set["ceilSize"] // 2
            keyx2 = str(int(set["player"]['posx']) - i - 1 + corectx)
            keyy2 = str(int(set["player"]['posy']) + j - 1 + corecty)

            x3 = w // 2 - i * set["ceilSize"] - (set["player"]['posx'] % 1) * set["ceilSize"] - set["ceilSize"] // 2
            y3 = h // 2 - j * set["ceilSize"] - (set["player"]['posy'] % 1) * set["ceilSize"] - set["ceilSize"] // 2
            keyx3 = str(int(set["player"]['posx']) - i - 1 + corectx)
            keyy3 = str(int(set["player"]['posy']) - j - 1 + corecty)

            x4 = w // 2 + i * set["ceilSize"] - (set["player"]['posx'] % 1) * set["ceilSize"] - set["ceilSize"] // 2
            y4 = h // 2 - j * set["ceilSize"] - (set["player"]['posy'] % 1) * set["ceilSize"] - set["ceilSize"] // 2
            keyx4 = str(int(set["player"]['posx']) + i - 1 + corectx)
            keyy4 = str(int(set["player"]['posy']) - j - 1 + corecty)

            # Рисуем все клеточки на каждой части экрана
            drawImgs(x1, y1, keyx1, keyy1, sc)
            drawImgs(x2, y2, keyx2, keyy2, sc)
            drawImgs(x3, y3, keyx3, keyy3, sc)
            drawImgs(x4, y4, keyx4, keyy4, sc)

    # Отображение колизий на f1
    if set["showCollisions"]:
        # Создание колизии для игрока
        x = w // 2 - set["ceilSize"] // 2
        y = h // 2 - set["ceilSize"] // 2
        pg.draw.circle(sc, (255, 255, 255), (x, y), 5)
        pg.draw.rect(sc, (255, 255, 255),
                     (w / 2 - set["ceilSize"] / 2, h / 2 - set["ceilSize"] / 2, set["ceilSize"], set["ceilSize"]), 1)
        for i in collisions:
            x = w // 2 + i[0][0] * set["ceilSize"] - (set["player"]["posx"]) * set["ceilSize"] - set["ceilSize"] // 2
            y = h // 2 + i[0][1] * set["ceilSize"] - (set["player"]["posy"]) * set["ceilSize"] - set["ceilSize"] // 2
            w2 = i[0][2] * set["ceilSize"]
            h2 = i[0][3] * set["ceilSize"]
            # Колизии для стен
            if i[1] == "stop":
                color = (255, 0, 0)
            # Колизии для генерации новой комнаты
            elif i[1] == "generate":
                color = (0, 255, 0)
            pg.draw.circle(sc, color, (x, y), 5)
            pg.draw.rect(sc, color, (x, y, w2, h2), 1)
    # Отрисовка мобов
    for i in mobs:
        x = w // 2 + i.pos[0] * set["ceilSize"] - (set["player"]["posx"]) * set["ceilSize"] - set["ceilSize"] // 2
        y = h // 2 + i.pos[1] * set["ceilSize"] - (set["player"]["posy"]) * set["ceilSize"] - set["ceilSize"] // 2
        sc.blit(pg.transform.scale(set["textures"]["entity"][i.texture], (set["ceilSize"], set["ceilSize"])), (x, y))

    # Отрисовка игрока
    if (set["player"]["speedx"] != 0) or (set["player"]["speedy"] != 0):
        sc.blit(pg.transform.flip(pg.transform.scale(playAnimation("player", 30), (set["ceilSize"], set["ceilSize"])),
                                  set["player"]["rotate"], False), (w / 2 - set["ceilSize"] / 2, h / 2 - set["ceilSize"] / 2))
    else:
        sc.blit(pg.transform.flip(pg.transform.scale(set["player"]["texture"], (set["ceilSize"], set["ceilSize"])),
                                  set["player"]["rotate"], False), (w / 2 - set["ceilSize"] / 2, h / 2 - set["ceilSize"] / 2))

    # health bar
    pg.draw.rect(sc, (255, 204, 204), (100, 930, 300, 30))
    pg.draw.rect(sc, (255, 51, 51), (100, 930, (300 / 100) * set["player"]['health'], 30))

    # Координаты и ФПС
    img1 = font.render("X:" + str(int(set["player"]['posx'])) + " Y:" + str(int(set["player"]['posy'])), True, (0, 0, 0))
    img2 = font.render("FPS:" + str(int(fps)), True, (0, 0, 0))
    sc.blit(img1, (100, 360))
    sc.blit(img2, (100, 390))

    # ОТрисовка миникарты
    draw_minimap(sc)

    # Отрисовка паузы
    if set["ONPAUSE"]:
        draw_onpause(sc)

    # Обновление экрана
    pg.display.flip()


# Функция открисовки миникарты
def draw_minimap(sc):
    pg.draw.rect(sc, (40, 40, 40),
                 (set["MINIMAP"][0] - 5, set["MINIMAP"][0] - 5, set["MINIMAP"][1] + 10, set["MINIMAP"][1] + 10))
    pg.draw.rect(sc, (80, 80, 80), (set["MINIMAP"][0], set["MINIMAP"][0], set["MINIMAP"][1], set["MINIMAP"][1]))

    for i in world_map:
        for j in world_map[i]:
            # Координаты и размеры комнаты на миникарте (создание самих комнат)
            coord = [
                [
                    int(i) * (set["MINIMAP"][2]) + set["MINIMAP"][1] // 2 - (set["player"]["posx"]) * (
                            set["MINIMAP"][2] / (set["roomSize"] * 2 + 6)) - 4 + 12.5,
                    int(j) * (set["MINIMAP"][2]) + set["MINIMAP"][1] // 2 - (set["player"]["posy"]) * (
                            set["MINIMAP"][2] / (set["roomSize"] * 2 + 6)) - 4 + 12.5,
                    set["MINIMAP"][2] - 25,
                    set["MINIMAP"][2] - 25
                ],
                [
                    int(i) * (set["MINIMAP"][2]) + set["MINIMAP"][1] // 2 - (set["player"]["posx"]) * (
                            set["MINIMAP"][2] / (set["roomSize"] * 2 + 6)) - 4,
                    int(j) * (set["MINIMAP"][2]) + set["MINIMAP"][1] // 2 - (set["player"]["posy"]) * (
                            set["MINIMAP"][2] / (set["roomSize"] * 2 + 6)) - 4 + 6.25 + (set["MINIMAP"][2] - 25) // 2,
                    set["MINIMAP"][2],
                    12.5
                ],
                [
                    int(i) * (set["MINIMAP"][2]) + set["MINIMAP"][1] // 2 - (set["player"]["posx"]) * (
                            set["MINIMAP"][2] / (set["roomSize"] * 2 + 6)) - 4 + 6.25 + (set["MINIMAP"][2] - 25) // 2,
                    int(j) * (set["MINIMAP"][2]) + set["MINIMAP"][1] // 2 - (set["player"]["posy"]) * (
                            set["MINIMAP"][2] / (set["roomSize"] * 2 + 6)) - 4,
                    12.5,
                    set["MINIMAP"][2]
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
                if (d[0] >= set["MINIMAP"][1] + set["MINIMAP"][0]):
                    d[0] = set["MINIMAP"][1] + set["MINIMAP"][0]
                    d[2] = 0
                    d[3] = 0
                elif (d[0] + d[2] >= set["MINIMAP"][1] + set["MINIMAP"][0]):
                    d[2] = set["MINIMAP"][1] + set["MINIMAP"][0] - d[0] + 1

                if (d[0] <= set["MINIMAP"][0]):
                    d[2] -= abs(d[0] - set["MINIMAP"][0])
                    d[0] = set["MINIMAP"][0]

                if (d[1] >= set["MINIMAP"][1] + set["MINIMAP"][0]):
                    d[1] = set["MINIMAP"][1] + set["MINIMAP"][0]
                    d[2] = 0
                    d[3] = 0
                elif (d[1] + d[3] >= set["MINIMAP"][1] + set["MINIMAP"][0]):
                    d[3] = set["MINIMAP"][1] + set["MINIMAP"][0] - d[1] + 1

                if (d[1] <= set["MINIMAP"][0]):
                    d[3] -= abs(d[1] - set["MINIMAP"][0])
                    d[1] = set["MINIMAP"][0]

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
    pg.draw.circle(sc, (255, 0, 0), (set["MINIMAP"][0] + set["MINIMAP"][1] // 2, set["MINIMAP"][0] + set["MINIMAP"][1] // 2), 4)
