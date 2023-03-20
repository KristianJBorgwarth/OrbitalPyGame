import pygame
from enum import Enum
from DesignPatterns.ComponentPattern import Component
from Scripts.CoreComponents import Transform, Animator
from Scripts.animation import Animation

class Layers(Enum):
    BACKGROUND = 0
    MIDDLEGROUND = 1
    FOREGROUND = 2

class GameObject:
    def __init__(self, x, y, image_path, world, layer: Layers):
        self.initial_position = pygame.math.Vector2(x, y)
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.world = world
        self.components = []
        self.layer = layer
        self.transform = Transform(position=(x, y), owner_go=self)
        self.add_component(self.transform)
        

    def update(self):
        keys = pygame.key.get_pressed()
        for comp in self.components:
            if isinstance(comp, Animator):
                if len(comp.animations_list) <= 0:
                    return

            comp.update()
        self.screen_wrap()

    def draw(self, screen):
        from Scripts.Projectile import BaseProjectile
        
        if self.get_component(Animator):
            img_copy = pygame.transform.rotate(self.get_component(Animator).get_current_frame(),
                                               self.transform.rotation)
            screen.blit(img_copy, (self.transform.position.x - int(img_copy.get_width() / 2),
                                   self.transform.position.y - int(img_copy.get_height() / 2)))
        else:
            center_x = self.transform.position.x - int(self.image.get_width() / 2)
            center_y = self.transform.position.y - int(self.image.get_height() / 2)
            # Draw the sprite image at its center
            screen.blit(self.image, (center_x, center_y))

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

    def screen_wrap(self):
        current_pos = self.transform.position
        
        # TODO: Move this into Components make it overrideable?

        from Scripts.Projectile import BaseProjectile
        if self.get_component(BaseProjectile) is not None:
            if current_pos.x > self.world.width + 50:
                self.world.destroy_go(self)
            elif current_pos.x < -50:
                self.world.destroy_go(self)
            elif current_pos.y > self.world.height + 50:
                self.world.destroy_go(self)
            elif current_pos.y < -50:
                self.world.destroy_go(self)

        else:
            if current_pos.x > self.world.width + 50:
                self.transform.position.x = -50
            elif current_pos.x < -50:
                self.transform.position.x = self.world.width + 50
            elif current_pos.y > self.world.height + 50:
                self.transform.position.y = -50
            elif current_pos.y < -50:
                self.transform.position.y = self.world.height + 50
