import pygame
from enum import Enum

from Scripts.DesignPatterns.CollisionPattern import CollisionHandler
from Scripts.DesignPatterns.ComponentPattern import Component
from Scripts.Components.CoreComponents import Transform, Animator


class Layers(Enum):
    BACKGROUND = 0
    MIDDLEGROUND = 1
    FOREGROUND = 2


class GameObject:
    def __init__(self, x, y, image_path, world, layer: Layers, tag):
        self.initial_position = pygame.math.Vector2(x, y)
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.world = world
        self.components = []
        self.layer = layer
        self.transform = Transform(position=(x, y), owner_go=self)
        self.add_component(self.transform)
        self.tag = tag
        self.collision_color = pygame.Color(255, 0, 0)

    def update(self):
        for comp in self.components:
            if isinstance(comp, Animator):
                if len(comp.animations_list) <= 0:
                    return

            comp.update()
        self.screen_wrap()

    def draw(self, screen):
        if self.get_component(Animator):
            if self.get_component(Animator).current_anim is None: return
            if self.get_component(Animator).get_current_frame() is None: return
            img_copy = pygame.transform.rotate(self.get_component(Animator).get_current_frame(),
                                               self.transform.rotation)
            screen.blit(img_copy, (self.transform._position.x - int(img_copy.get_width() / 2),
                                   self.transform.position.y - int(img_copy.get_height() / 2)))
        else:
            center_x = self.transform.position.x - int(self.image.get_width() / 2)
            center_y = self.transform.position.y - int(self.image.get_height() / 2)
            # Draw the sprite image at its center
            screen.blit(self.image, (center_x, center_y))

    def handle_collision(self, other_go, collision_type):
        collision_handler = self.get_component(CollisionHandler)

        if collision_handler is not None:
            if collision_type == "enter":
                collision_handler.on_collision_enter(other_go)
            elif collision_type == "stay":
                collision_handler.on_collision(other_go)
            elif collision_type == "exit":
                collision_handler.on_collision_exit(other_go)

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

    def add_collision_rule(self, tag):
        collision_handler = self.get_component(CollisionHandler)

        if collision_handler is not None:
            collision_handler.add_collision_rule(tag)

    def serialize_gameobject(self, go_name):
        components_dict = [c.serialize() for c in self.components]
        return {'name': go_name, 'initial_position': {'x': self.initial_position.x, 'y': self.initial_position.y},
                'image_path': self.image_path, 'components': components_dict}

    def screen_wrap(self):
        current_pos = self.transform.position

        # TODO: Move this into Components make it overrideable?

        from Scripts.Components.Projectile import BaseProjectile
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

            coll = self.get_component(CollisionHandler)
            if current_pos.x > self.world.width + 50:
                self.transform.position.x = -50
            elif current_pos.x < -50:
                self.transform.position.x = self.world.width + 50
            elif current_pos.y > self.world.height + 50:
                self.transform.position.y = -50
            elif current_pos.y < -50:
                self.transform.position.y = self.world.height + 50


