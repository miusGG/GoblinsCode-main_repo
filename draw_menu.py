import pygame


pygame.mixer.init()

#Класс создания кнопки
class ImageButton:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.text = text
        self.height = height

        self.image = pygame.image.load("game/textures/gui/" + image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load("game/textures/gui/" + hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound("game/sounds/" + sound_path)
            self.sound.set_volume(0.5)
        self.is_hovered = False

    #Отрисовка
    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    #Проверка где курсор
    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    #Проигрывает звук при нажатии на кнопку
    def handle_event(self, event, inGame):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
                if self.sound:
                    self.sound.play()
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))