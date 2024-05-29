import pygame
import os
class MenuSettings():

    def __init__(self, aw_settings, screen, text, pos):
        self.aw_settings = aw_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        image = pygame.image.load(self.aw_settings.path_to_img + os.sep + "bg_settings.png")
        self.bg_set_img = pygame.transform.scale(image, (self.aw_settings.menu_settings_width, self.aw_settings.menu_settings_height))
        self.bg_rect = self.bg_set_img.get_rect()
        self.bg_rect.center = self.screen_rect.center


        self.hovered = False
        self.width, self.height = self.aw_settings.menu_button_width, self.aw_settings.menu_button_height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.text = text
        self.pos = pos
        self.font = pygame.font.SysFont("Verdana", 40)
        self.text_color = (100, 154, 252)
        self.text_color_hovered = (0, 0, 255)
        self.sound_lim = 0

        self.volume_button_pos = (self.bg_rect.centerx, self.aw_settings.menu_settings_height)
        self.back_button_pos = (self.bg_rect.centerx, self.bg_rect.bottom)
        self.draw()

    def blitme(self):
        self.screen.blit(self.bg_set_img, self.bg_rect)

    def draw(self):
        if self.hovered:
            self.point = self.font.render(self.text, True, self.text_color_hovered)
        else:
            self.point = self.font.render(self.text, True, self.text_color)
        self.rect.centerx, self.rect.top = self.pos
        self.point_rect = self.point.get_rect()
        self.point_rect.centerx = self.rect.centerx
        self.point_rect.centerx, self.point_rect.top = self.pos
        self.screen.blit(self.point, self.point_rect)