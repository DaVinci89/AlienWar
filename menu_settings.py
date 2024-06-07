import pygame
class MenuSettings():

    def __init__(self, aw_settings, screen, text, pos, bground_settings):
        self.aw_settings = aw_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.bg = bground_settings
        self.hovered = False
        self.width, self.height = self.aw_settings.menu_button_width, self.aw_settings.menu_button_height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.text = text
        self.pos = pos
        self.font = pygame.font.SysFont("Verdana", 25)
        self.text_color = (100, 154, 252)
        self.text_color_hovered = (0, 0, 255)
        self.sound_lim = 0
        self.bg_rect = self.bg.bg_rect
        self.volume_button_pos = (self.bg_rect.centerx, self.bg_rect.centery - self.aw_settings.menu_button_height)
        self.back_button_pos = (self.bg_rect.centerx, self.bg_rect.bottom - self.aw_settings.menu_button_height)
        self.draw()



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