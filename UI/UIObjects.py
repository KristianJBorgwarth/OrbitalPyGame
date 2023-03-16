import pygame


class UIObject:
    def __init__(self, world, x, y):
        self.is_enabled = True
        self.position = pygame.math.Vector2(x, y)
        self.components = []
        self.world = world
        self.tag = ""

    def update(self):
        if self.is_enabled is False: return
        for comp in self.components: comp.update()

    def draw(self, screen):
        if self.is_enabled is False: return
        for comp in self.components: comp.draw(screen)

    def on_enable(self):
        self.is_enabled = True

    def on_disable(self):
        self.is_enabled = False

    def add_component(self, component):
        if self.components.__contains__(component):
            return
        else:
            self.components.append(component)

    def get_component(self, component):
        for comp in self.components:
            if isinstance(comp, component):
                return comp
        return None
