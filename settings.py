import pygame as pg
from draw_menu import ImageButton


#Все настройки игры.
set = {
    "FPS" : 0,
    "INGAME" : False,
    "INMENU" : True,
    "INSETTINGS" : False,
    "INVIDEOSETTINGS" : False,
    "ONPAUSE" : False,
    "OPENEDMAP" : False,
    "DISPLAY" : [1920, 1080],
    "MINIMAP" : [50, 300, 100],
    "WINNAME" : "GoblinsGold",
    "countrooms" : 0,
    "ceilSize" : 100,
    "playerSize": 40,
    "roomSize" : 7,
    "showCollisions" : False,
    "showCurCoords" : False,
    "cx" : 0,
    "cy" : 0,
    "deth" : False,
    "player" : {
        "rotate" : False,
        "health": 100,
        "posx" : 0,
        "posy" : 0,
        "speedx" : 0,
        "speedy" : 0,
        "speed" : 10
    },
    "none_texture" : "dirt.png",
    "player_texture" : "playerstay.png",
    "animations":{
        "player":[
            "entity/playerwalk1.png",
            "entity/playerwalk2.png"
        ],
        "bleb":[
            "entity/slime.png",
            "entity/slime2.png",
            "entity/slime3.png"
        ]
    },
    "textures": {
        "gui" : {

        },
        "animations":{

        },
        "structures" : {

        },"items" : {

        },"entity" : {

        }, "secondLayer": {

        }
    },
    "object": {
        "gui" :{
            "mainPicture" : "GoblinASS2.png",
            "settingsPicture" : "GoblinASS.png"
        },
        "structures": {
            "dirt" : "dirt.png",
            "dirtwithwall" : "dirtwithwall.png",
            "dirtwithcorner" : "dirtwithcorner.png",
            "dirtwithcorner2" : "dirtwithcorner2.png",
            "darkfade" : "darkfade.png",
            "darkfadewithcorner" : "darkfadewithcorner.png"
        }, "items": {

        }, "entity": {
            "bleb": "bleb.png",
            "frog": "frog.jpg",
            "slime": "slime.png"
        }, "secondLayer": {
            "frog" : "frog.jpg"
        }

    }, "entity_damage_triggers": {
            "bleb_options": {
                "bleb-trigger": False,
                "bled-damage": 100,
                "bleb-kd": 14000
            }
    }
}

WIDTH, HEIGHT = set["DISPLAY"]

#Кноки под каждое меню
buttons = {
    "start" : ImageButton(WIDTH - HEIGHT, HEIGHT / 2.5, WIDTH/6, HEIGHT/9, "НАЧАТЬ ИГРУ", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3"),
    "exit" : ImageButton(WIDTH - HEIGHT, HEIGHT / 1.47, WIDTH/6, HEIGHT/9, "ВЫЙТИ", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3"),
    "settings" : ImageButton(WIDTH - HEIGHT, HEIGHT / 1.85, WIDTH/6, HEIGHT/9, "НАСТРОЙКИ", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3"),
}

buttonsSettings = {
    "video_set": ImageButton(WIDTH - HEIGHT, HEIGHT / 2.5, WIDTH/6, HEIGHT/9, "ВИДЕО", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3"),
    "volme_set": ImageButton(WIDTH - HEIGHT, HEIGHT / 1.47, WIDTH/6, HEIGHT/9, "ЗВУК", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3"),
    "exit_from_settings": ImageButton(WIDTH - HEIGHT, HEIGHT / 1.26, WIDTH/6, HEIGHT/9, "ВЫЙТИ", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3"),
    "keys_set": ImageButton(WIDTH - HEIGHT, HEIGHT / 1.85, WIDTH/6, HEIGHT/9, "УПРАВЛЕНИЕ", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3")
}

buttonVideoSettings = {
    "hightVideo" : ImageButton(WIDTH - HEIGHT, HEIGHT / 2.5, WIDTH/6, HEIGHT/9, "Hight", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3"),
    "lowVideo" : ImageButton(WIDTH - HEIGHT, HEIGHT / 1.47, WIDTH/6, HEIGHT/9, "Low", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3"),
    "mediumVideo" : ImageButton(WIDTH - HEIGHT, HEIGHT / 1.85, WIDTH/6, HEIGHT/9, "Medium", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3"),
    "exit_from_video_settings": ImageButton(WIDTH - HEIGHT, HEIGHT / 1.26, WIDTH/6, HEIGHT/9, "ВЫЙТИ", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3")
}


ingamebuttons = {
    "exit_from_game" : ImageButton(WIDTH/2-(252/2), 450, 302, 124, "ВЫЙТИ", "startGame-button.png", "startGame-button_hoverd.png", "button_click.mp3")
}

# Функция для загрузки всех текстур
def load():
    set["player"]["texture"] = pg.image.load("game/textures/entity/" + set["player_texture"])
    for i in set["animations"]:
        set["textures"]["animations"][i] = []
        for j in set["animations"][i]:
            set["textures"]["animations"][i].append(pg.image.load("game/textures/" + j))

    for i in set["object"]:
        for j in set["object"][i]:
            set["textures"][i][j] = pg.image.load("game/textures/" + i + "/" + set["object"][i][j]).convert_alpha()