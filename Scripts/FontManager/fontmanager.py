import pygame.font

import globals


class FontManager:
    def __init__(self, font):
        self.font = pygame.font.Font(font, 24)

    def render_font(self, text, position, screen, color):
        current_color = globals.WHITE

        if color.lower() == "black":
            current_color = globals.BLACK
        elif color.lower() == "red":
            current_color = globals.RED
        elif color.lower() == "green":
            current_color = globals.GREEN
        elif color.lower() == "blue":
            current_color = globals.BLUE
        else:
            current_color = globals.WHITE

        text_surface = self.font.render(text, True, current_color)
        screen.blit(text_surface, position)

    def get_text_width(self, text):
        text_surface = self.font.render(text, True, (0, 0, 0))  # color doesn't matter
        text_width, _ = text_surface.get_size()
        return text_width

    def get_text_height(self, text):
        text_surface = self.font.render(text, True, (0, 0, 0))  # color doesn't matter
        _, text_height = text_surface.get_size()
        return text_height