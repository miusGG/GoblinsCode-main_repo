import pygame as pg

class Mob():
    def __init__(self, texture, cor, health, weapon, ai=None):
        self.health = health
        self.texture = texture
        self.weapon = weapon
        self.pos = [
            cor[0],
            cor[1]
        ]
        self.speed = [
            0,
            0
        ]
        self.ai = ai

    #Добавление ИИ.
    def addAI(self, ai):
        self.ai = ai

    #Обновление ИИ
    def updateAI(self, ingame, onpause):
        if self.ai != None and ingame and not onpause:
            self.ai()

#Все мобы
mobs = []


class MobNow(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

import createmobs