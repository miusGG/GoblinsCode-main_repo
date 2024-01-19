import sys
import pygame as pg

from settings import set
from funcs import checkCollisionx, checkCollisiony
from settings import buttons, buttonsSettings, ingamebuttons, buttonVideoSettings, LastMenubButtons
from generate import gen, clearWorld
from mob import mobs


# Обновление ИИ мобов.
def mobsAI():
    for i in mobs:
        i.updateAI(set["INGAME"], set["ONPAUSE"])


# Тип инвентов для получения урона
BLEBDAMAGEEVENT, timer = pg.USEREVENT + 1, set["entity_damage_triggers"]["bleb_options"]["bleb-kd"]


# Функция ИВЕНТОВ
def event(fps):
    for run in pg.event.get():
        if run.type == pg.QUIT:
            sys.exit()

        # Кнопки для МЕНЮ
        if set["INMENU"]:
            for j in buttons:
                buttons[j].handle_event(run, set["INGAME"])
                buttons[j].check_hover(pg.mouse.get_pos())

                if run.type == pg.USEREVENT and run.button == buttons["start"]:
                    set["INGAME"] = True
                    set["INMENU"] = False
                    gen.generateRoom((0, 0), [2, -1])

                if run.type == pg.USEREVENT and run.button == buttons["settings"]:
                    set["INMENU"] = False
                    set["INSETTINGS"] = True

                if run.type == pg.USEREVENT and run.button == buttons["exit"]:
                    pg.quit()

        # Кнопки для настроек
        if set["INSETTINGS"]:
            for j in buttonsSettings:
                buttonsSettings[j].handle_event(run, set["INGAME"])
                buttonsSettings[j].check_hover(pg.mouse.get_pos())

                if run.type == pg.USEREVENT and run.button == buttonsSettings["exit_from_settings"]:
                    set["INSETTINGS"] = False
                    set["INMENU"] = True

                if run.type == pg.USEREVENT and run.button == buttonsSettings["video_set"]:
                    set["INSETTINGS"] = False
                    set["INVIDEOSETTINGS"] = True

        # Кнопки для настроек видео
        if set["INVIDEOSETTINGS"]:
            for j in buttonVideoSettings:
                buttonVideoSettings[j].handle_event(run, set["INGAME"])
                buttonVideoSettings[j].check_hover(pg.mouse.get_pos())

                if run.type == pg.USEREVENT and run.button == buttonVideoSettings['hightVideo']:
                    pass

                if run.type == pg.USEREVENT and run.button == buttonVideoSettings['lowVideo']:
                    pass

                if run.type == pg.USEREVENT and run.button == buttonVideoSettings['mediumVideo']:
                    pass

                if run.type == pg.USEREVENT and run.button == buttonVideoSettings['exit_from_video_settings']:
                    set["INSETTINGS"] = True
                    set["INVIDEOSETTING"] = False

        # Кнопки для паузы
        if set["ONPAUSE"] and set["INGAME"]:
            for j in ingamebuttons:
                ingamebuttons[j].handle_event(run, set["INGAME"])
                ingamebuttons[j].check_hover(pg.mouse.get_pos())

                if run.type == pg.USEREVENT and run.button == ingamebuttons["exit_from_game"]:
                    clearWorld()
                    mobs.clear()
                    set["INGAME"] = False
                    set["ONPAUSE"] = False
                    set["INMENU"] = True

        if set["lastRoom"]:
            set["INGAME"] = False
            set["ONPAUSE"] = False
            set["deth"] = False

            for j in LastMenubButtons:
                LastMenubButtons[j].handle_event(run, set["INGAME"])
                LastMenubButtons[j].check_hover(pg.mouse.get_pos())

                if run.type == pg.USEREVENT and run.button == LastMenubButtons["exit_to_menu"]:
                    clearWorld()
                    set["INGAME"] = False
                    set["ONPAUSE"] = False
                    set["INMENU"] = True

        # Если СМЭЭЭРТъ!
        if set["deth"]:
            for j in ingamebuttons:
                ingamebuttons[j].handle_event(run, set["INGAME"])
                ingamebuttons[j].check_hover(pg.mouse.get_pos())

                # Тут мы убираем все тригеры дамага
                set["entity_damage_triggers"]["bleb_options"]["bleb-trigger"] = False

                set["player"]["health"] = 100

                clearWorld()
                mobs.clear()

                set["INGAME"] = False
                set["ONPAUSE"] = False
                set["INMENU"] = False

                if run.type == pg.USEREVENT and run.button == ingamebuttons["exit_from_game"]:
                    set["deth"] = False
                    set["INGAME"] = False
                    set["ONPAUSE"] = False
                    set["INMENU"] = True

        if run.type == pg.USEREVENT and run.button == buttons["exit"]:
            pg.quit()

        # Если крутиться колёсико мышки то клетки УВЕЛИЧИВАЮТСЯ или УМЕНЬШАЮТСЯ в ширину или в длинну
        if run.type == pg.MOUSEWHEEL:
            if (set["ceilSize"] + run.y * 2 > 0) and (not set["ONPAUSE"]):
                set["ceilSize"] += run.y * 2
        if run.type == pg.MOUSEMOTION:
            set["cx"] = run.pos[0]
            set["cy"] = run.pos[1]

        # События для получения урона от мобов
        if run.type == BLEBDAMAGEEVENT and set["entity_damage_triggers"]["bleb_options"]["bleb-trigger"]:
            set["player"]["health"] = set["player"]["health"] - set["entity_damage_triggers"]["bleb_options"]["bled-damage"]
            set["deth"] = True
            set["INGAME"] = False
            set["INMENU"] = False

        # Если кнопка НАЖАТА то игрок может ходить
        if run.type == pg.KEYDOWN:
            if run.key == pg.K_ESCAPE:
                if set["INGAME"]:
                    if set["ONPAUSE"]:
                        set["ONPAUSE"] = False
                    else:
                        set["ONPAUSE"] = True
            if run.key == pg.K_TAB:
                set["MINIMAP"][1] = 1000

            # При нажатии F1 показываются КОЛЛИЗИИИ
            if run.key == pg.K_F1:
                set["showCollisions"] = not set["showCollisions"]

            if run.key == pg.K_w:
                set["player"]["speedy"] -= set["player"]["speed"]
            if run.key == pg.K_a:
                set["player"]["speedx"] -= set["player"]["speed"]
            if run.key == pg.K_s:
                set["player"]["speedy"] += set["player"]["speed"]
            if run.key == pg.K_d:
                set["player"]["speedx"] += set["player"]["speed"]

        # Если кнопка ОТЖАТА то игрок теряет скорость
        if run.type == pg.KEYUP:
            if run.key == pg.K_TAB:
                set["MINIMAP"][1] = 300
            if run.key == pg.K_w:
                set["player"]["speedy"] += set["player"]["speed"]
            if run.key == pg.K_a:
                set["player"]["speedx"] += set["player"]["speed"]
            if run.key == pg.K_s:
                set["player"]["speedy"] -= set["player"]["speed"]
            if run.key == pg.K_d:
                set["player"]["speedx"] -= set["player"]["speed"]

    # проверка есть ли туда куда хочет пойти игрок припятствие
    if not set["ONPAUSE"]:
        if ((set["player"]["speedx"] != 0) or (set["player"]["speedy"] != 0)) and (fps != 0):
            if checkCollisionx(set["player"]["posx"] + set["player"]["speedx"] / fps):
                set["player"]["posx"] += set["player"]["speedx"] / fps
            if checkCollisiony(set["player"]["posy"] + set["player"]["speedy"] / fps):
                set["player"]["posy"] += set["player"]["speedy"] / fps
        if set["player"]["speedx"] > 0:
            set["player"]["rotate"] = False
        elif set["player"]["speedx"] < 0:
            set["player"]["rotate"] = True
