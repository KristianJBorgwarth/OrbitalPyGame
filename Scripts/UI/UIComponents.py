import pygame.image
from overrides import overrides, override

from Scripts.DesignPatterns.ComponentPattern import Component


class UIComponent(Component):
    def __init__(self, game_object, image):
        super().__init__(game_object)
        self.image = pygame.image.load(image)
        self.go = game_object
        self.rect = self.image.get_rect()
        self.rect.x = game_object.position.x
        self.rect.y = game_object.position.y

    @override
    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.go.position)


class UIButton(UIComponent):
    def __init__(self, game_object, image, hover_image, event):
        super().__init__(game_object, image)
        self.hover_image = pygame.image.load(hover_image)
        self.original_image = self.image
        self.event = pygame.event.Event(event)
        self.go.tag = "button"

    def update(self):
        self.on_hover()
        self.on_click()

    def draw(self, screen):
        super().draw(screen)

    def on_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.hover_image
        else:
            self.image = self.original_image

    def on_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_button_pressed = pygame.mouse.get_pressed()[0]
        if self.rect.collidepoint(mouse_pos) and left_button_pressed:
            pygame.event.post(self.event)


class BackGround(UIComponent):
    def __init__(self, game_object, image):
        super().__init__(game_object, image)
        self.go.tag = "background"

    def update(self):
        self.scroll_backGround()

    @overrides
    def draw(self, screen):
        screen.blit(self.image, self.go.position)
        screen.blit(self.image, (self.go.position.x, self.go.position.y - self.image.get_height()))

    def scroll_backGround(self):
        scroll_speed = 5
        self.go.position.y += scroll_speed
        if self.go.position.y > self.image.get_height():
            self.go.position.y = 0
