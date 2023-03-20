import os
import pygame
from overrides import override

import globals
from DesignPatterns.ComponentPattern import Component
from Scripts.CoreComponents import Animator
from Scripts.GameObject import GameObject
from Scripts.PhysicsComponents import Rigidbody
from Scripts.animation import Animation


class Player(Component):
    def __init__(self, owner_go: GameObject):
        super().__init__(owner_go)

        self.owner = owner_go
        self.rigidbody = self.owner.get_component(Rigidbody)
        self.projectile_dir = os.path.join(self.owner.world.project_dir
                                           )

        self.directions = \
            {
                'x': {'positive': pygame.K_h, 'negative': pygame.K_k},
                'y': {'positive': pygame.K_DOWN, 'negative': pygame.K_UP},
            }

    def serialize(self):
        d = super().serialize()
        d.update({
            'type': self.__class__.__name__,
        })
        return d

    @classmethod
    @override
    def deserialize(cls, d: dict, owner_go) -> 'Player':
        pass

    @override
    def update(self):
        super().update()

        keys = pygame.key.get_pressed()
        # keys_down stores the value of pygames events
        keys_down = pygame.event.get()
        # Quit on escape
        #loops through the keys_down events
        for k in keys_down:
            #checks the type of event this is for keys that are held down
            if k.type == pygame.KEYDOWN:
                #check if the key held down is space
                if k.key == pygame.K_SPACE:
                    #sets key repeating delay , interval before being able to run this again
                    pygame.key.set_repeat(1, 500 )
                    globals.soundManager.play_sound("shoot")
        if keys[pygame.K_LEFT]:
            comp = self.owner.get_component(Animator).current_anim
            if comp != None:
                self.owner.transform.rotate_image(comp, -6)
        if keys[pygame.K_RIGHT]:
            comp = self.owner.get_component(Animator).current_anim
            if comp != None:
                self.owner.transform.rotate_image(comp, 6)

        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            return

        if self.rigidbody is None:
            return

        #self.rigidbody.update_velocity('x', keys, self.directions, self.owner)
        self.rigidbody.update_velocity('y', keys, self.directions, self.owner)

        if self.rigidbody.velocity.magnitude() > 0.0:
            print(f"Velocity > x: {self.rigidbody.velocity.x.__round__()}, y: {self.rigidbody.velocity.y.__round__()}")



