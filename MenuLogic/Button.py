import pygame
from overrides import override
from GameObject import GameObject


class Button(GameObject):
    def __init__(self, x, y, image, world, text, command):
        super().__init__(x, y, image, world)
        self.button_command = command
        self.color = (27, 27, 27)
        self.hoverColor = (79, 79, 79)
        self.text = text
        self.text_color = (255, 255, 255)
        self.font_size = 50
        self.font = pygame.font.SysFont(None, self.font_size)
        self.rect = pygame.Rect(x, y, 400, 100)
        self.canClick = False
        self.pressBlock = False

    @override
    def update(self):
        self.check_hover_on_button()
        self.execute_on_press()
        self.reset_canPress()

    @override
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def execute_on_press(self):
        if self.canClick and pygame.mouse.get_pressed()[0] and self.pressBlock == False:
            self.button_command.execute()
            self.pressBlock = True

    def reset_canPress(self):
        if not pygame.mouse.get_pressed()[0]:
            self.pressBlock = False

    def check_hover_on_button(self):
        mouse_rect = pygame.Rect(*pygame.mouse.get_pos(), 1, 1)
        if self.rect.colliderect(mouse_rect):
            self.color = self.hoverColor
            self.canClick = True
        else:
            self.color = (27, 27, 27)
            self.canClick = False
