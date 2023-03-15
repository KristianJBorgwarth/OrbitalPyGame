import pygame

from DesignPatterns.ComponentPattern import Component
from Scripts.CoreComponents import Transform


class GameObject:
    def __init__(self, x, y, image_path, world):
        self.initial_position = pygame.math.Vector2(x, y)
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.world = world
        self.components = []
        self.transform = Transform(position=(x, y), owner_go=self)
        self.add_component(self.transform)

    def update(self):
        for comp in self.components:
            comp.update()

    def draw(self, screen):
        screen.blit(self.image, self.transform.position)

    def add_component(self, component: Component):
        if self.components.__contains__(component):
            return
        else:
            self.components.append(component)
        # elif not issubclass(component, Components):
        #     raise ValueError("component must be a subclass of Component!")

    def get_component(self, component_type):
        # Check if the component is in the list
        for comp in self.components:
            if isinstance(comp, component_type):
                # If it is return it
                return comp
        # Return none if it isn't
        return None

    def serialize_gameobject(self, go_name):
        components_dict = [c.serialize() for c in self.components]
        return {'name': go_name, 'initial_position': {'x': self.initial_position.x, 'y': self.initial_position.y},
                'image_path': self.image_path, 'components': components_dict}
