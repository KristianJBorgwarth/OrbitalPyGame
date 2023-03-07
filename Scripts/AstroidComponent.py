import random
from random import Random

import pygame.transform
from overrides import override
from DesignPatterns.ComponentPattern import Component
from Scripts.GameObject import GameObject
from Scripts.PhysicsComponents import Rigidbody


class Astroid(Component):

    def __init__(self, owner_go: GameObject):
        super().__init__(owner_go)
        self.owner = owner_go
        self.rigidbody = self.owner.get_component(Rigidbody)



    def serialize(self):
        d = super().serialize()
        d.update({
            'type': self.__class__.__name__,

        })
        return d

    @classmethod
    def deserialize(cls, d: dict, owner_go) -> 'Astroid':
        pass

    @override
    def update(self):
        super().update()
        self.rigidbody.add_force((1, 1), self.owner)



