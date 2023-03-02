import pygame.image
from abc import abstractmethod, ABC
from overrides import override
import Components


class GameObject(ABC):
    def __init__(self, x, y, image, world):
        # self.transform = Transform(position=(x, y))
        self.add_component(Components.Transform(position=(x, y)))
        self.image = pygame.image.load(image)
        self.world = world
        self.components = []

    def update(self):
        for comp in self.components:
            comp.update()

    def draw(self, screen):
        screen.blit(self.image, self.transform.position)

    def add_component(self, component: Components):
        if self.components.__contains__(component):
            return
        
        self.components.append(component)
        
    def get_component(self, component: Components):
        # Check if the component is in the list
        for comp in self.components:
            if isinstance(comp, component):
                # If it is return it
                return comp
        # Return none if it isnt
        return None
