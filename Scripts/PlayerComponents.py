import os
import pygame
from overrides import override
from DesignPatterns.ComponentPattern import Component
from Scripts.GameObject import GameObject
from Scripts.PhysicsComponents import Rigidbody


class Player(Component):
    def __init__(self, owner_go: GameObject):
        super().__init__(owner_go)

        self.owner = owner_go
        self.rigidbody = self.owner.get_component(Rigidbody)
        self.projectile_dir = os.path.join(self.owner.world.project_dir
                                           )

        self.directions = \
            {
                'x': {'positive': pygame.K_RIGHT, 'negative': pygame.K_LEFT},
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

        # Quit on escape
        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            return

        if self.rigidbody is None:
            return

        self.rigidbody.update_velocity('x', keys, self.directions, self.owner)
        self.rigidbody.update_velocity('y', keys, self.directions, self.owner)

        if self.rigidbody.velocity.magnitude() > 0.0:
            print(f"Velocity > x: {self.rigidbody.velocity.x.__round__()}, y: {self.rigidbody.velocity.y.__round__()}")
