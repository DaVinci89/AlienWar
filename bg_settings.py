import pygame.image
import os

class Background_Settings():
    def __init__(self, aw_settings, screen):
        self.aw_settings = aw_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        image = pygame.image.load(self.aw_settings.path_to_img + os.sep + "bg_settings.png")
        self.bg_set_img = pygame.transform.scale(image, (self.aw_settings.menu_settings_width, self.aw_settings.menu_settings_height))
        self.bg_rect = self.bg_set_img.get_rect()
        self.bg_rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.bg_set_img, self.bg_rect)