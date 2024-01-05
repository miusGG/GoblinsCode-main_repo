import sys
import pygame as pg

from settings import set as s
from funcs import checkCollisionx, checkCollisiony
from settings import buttons, buttonsSettings, ingamebuttons, buttonVideoSettings
from generate import gen, clearWorld
from mob import mobs


# Обновление ИИ мобов.
def mobsAI():
    for i in mobs:
        i.updateAI(s["INGAME"], s["ONPAUSE"])


#Тип инвентов для получения урона
BLEBDAMAGEEVENT, timer = pg.USEREVENT+1, s["entity_damage_triggers"]["bleb_options"]["bleb-kd"]


#Функция ИВЕНТОВ
def event(fps):
    for run in pg.event.get():
        if run.type == pg.QUIT:
            sys.exit()

        #Кнопки для МЕНЮ
        if s["INMENU"]:
            for j in buttons:
                buttons[j].handle_event(run, s["INGAME"])
                buttons[j].check_hover(pg.mouse.get_pos())

                if run.type == pg.USEREVENT and run.button == buttons["start"]:
                    s["INGAME"] = True
                    s["INMENU"] = False
                    gen.generateRoom((0, 0), [2, -1])

                if run.type == pg.USEREVENT and run.button == buttons["settings"]:
                    s["INMENU"] = False
                    s["INSETTINGS"] = True

                if run.type == pg.USEREVENT and run.button == buttons["exit"]:
                    pg.quit()

        #Кнопки для настроек
        if s["INSETTINGS"]:
            for j in buttonsSettings:
                buttonsSettings[j].handle_event(run, s["INGAME"])
                buttonsSettings[j].check_hover(pg.mouse.get_pos())

                if run.type == pg.USEREVENT and run.button == buttonsSettings["exit_from_settings"]:
                    s["INSETTINGS"] = False
                    s["INMENU"] = True

                if run.type == pg.USEREVENT and run.button == buttonsSettings["video_set"]:
                    s["INSETTINGS"] = False
                    s["INVIDEOSETTINGS"] = True

        # Кнопки для настроек видео
        if s["INVIDEOSETTINGS"]:
            for j in buttonVideoSettings:
                buttonVideoSettings[j].handle_event(run, s["INGAME"])
                buttonVideoSettings[j].check_hover(pg.mouse.get_pos())

                if run.type == pg.USEREVENT and run.button == buttonVideoSettings['hightVideo']:
                    print(0)

                if run.type == pg.USEREVENT and run.button == buttonVideoSettings['lowVideo']:
                    print(0)

                if run.type == pg.USEREVENT and run.button == buttonVideoSettings['mediumVideo']:
                    print(0)

                if run.type == pg.USEREVENT and run.button == buttonVideoSettings['exit_from_video_settings']:
                    s["INSETTINGS"] = True
                    s["INVIDEOSETTING"] = False

        # Кнопки для паузы
        if s["ONPAUSE"] and s["INGAME"]:
            for j in ingamebuttons:
                ingamebuttons[j].handle_event(run, s["INGAME"])
                ingamebuttons[j].check_hover(pg.mouse.get_pos())

                if run.type == pg.USEREVENT and run.button == ingamebuttons["exit_from_game"]:
                    clearWorld()
                    s["INGAME"] = False
                    s["ONPAUSE"] = False
                    s["INMENU"] = True

        #Если СМЭЭЭРТъ!
        if s["deth"]:
            for j in ingamebuttons:
                ingamebuttons[j].handle_event(run, s["INGAME"])
                ingamebuttons[j].check_hover(pg.mouse.get_pos())

                #Тут мы убираем все тригеры дамага
                s["entity_damage_triggers"]["bleb_options"]["bleb-trigger"] = False

                s["player"]["health"] = 100

                clearWorld()

                s["INGAME"] = False
                s["ONPAUSE"] = False
                s["INMENU"] = False

                if run.type == pg.USEREVENT and run.button == ingamebuttons["exit_from_game"]:
                    s["deth"] = False
                    s["INGAME"] = False
                    s["ONPAUSE"] = False
                    s["INMENU"] = True

        if run.type == pg.USEREVENT and run.button == buttons["exit"]:
            pg.quit()

        # Если крутиться колёсико мышки то клетки УВЕЛИЧИВАЮТСЯ или УМЕНЬШАЮТСЯ в ширину или в длинну
        if run.type == pg.MOUSEWHEEL:
            if (s["ceilSize"] + run.y * 2 > 0) and (not s["ONPAUSE"]):
                s["ceilSize"] += run.y * 2
        if run.type == pg.MOUSEMOTION:
            s["cx"] = run.pos[0]
            s["cy"] = run.pos[1]

        #События для получения урона от мобов
        if run.type == BLEBDAMAGEEVENT and s["entity_damage_triggers"]["bleb_options"]["bleb-trigger"]:
            s["player"]["health"] = s["player"]["health"] - s["entity_damage_triggers"]["bleb_options"]["bled-damage"]
            s["deth"] = True
            s["INGAME"] = False
            s["INMENU"] = False

        # Если кнопка НАЖАТА то игрок может ходить
        if run.type == pg.KEYDOWN:
            if run.key == pg.K_ESCAPE:
                if s["INGAME"]:
                    if s["ONPAUSE"]:
                        s["ONPAUSE"] = False
                    else:
                        s["ONPAUSE"] = True
            if run.key == pg.K_TAB:
                s["MINIMAP"][1] = 1000

            # При нажатии F1 показываются КОЛЛИЗИИИ
            if run.key == pg.K_F1:
                s["showCollisions"] = not s["showCollisions"]

            if run.key == pg.K_w:
                s["player"]["speedy"] -= s["player"]["speed"]
            if run.key == pg.K_a:
                s["player"]["speedx"] -= s["player"]["speed"]
            if run.key == pg.K_s:
                s["player"]["speedy"] += s["player"]["speed"]
            if run.key == pg.K_d:
                s["player"]["speedx"] += s["player"]["speed"]

        # Если кнопка ОТЖАТА то игрок теряет скорость
        if run.type == pg.KEYUP:
            if run.key == pg.K_TAB:
                s["MINIMAP"][1] = 300
            if run.key == pg.K_w:
                s["player"]["speedy"] += s["player"]["speed"]
            if run.key == pg.K_a:
                s["player"]["speedx"] += s["player"]["speed"]
            if run.key == pg.K_s:
                s["player"]["speedy"] -= s["player"]["speed"]
            if run.key == pg.K_d:
                s["player"]["speedx"] -= s["player"]["speed"]


    # проверка есть ли туда куда хочет пойти игрок припятствие
    if not s["ONPAUSE"]:
        if ((s["player"]["speedx"] != 0) or (s["player"]["speedy"] != 0)) and (fps != 0):
            if (checkCollisionx(s["player"]["posx"] + s["player"]["speedx"] / fps)):
                s["player"]["posx"] += s["player"]["speedx"] / fps
            if (checkCollisiony(s["player"]["posy"] + s["player"]["speedy"] / fps)):
                s["player"]["posy"] += s["player"]["speedy"] / fps
        if (s["player"]["speedx"] > 0):
            s["player"]["rotate"] = False
        elif (s["player"]["speedx"] < 0):
            s["player"]["rotate"] = True
