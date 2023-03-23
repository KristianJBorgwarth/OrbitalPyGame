import pygame

from Scripts.DesignPatterns.ComponentPattern import Component
from Scripts.Core import GameObject


class BaseProjectile(Component):
    def __init__(self, owner_go: GameObject, damage, forward_dir, rotation):
        super().__init__(owner_go)
        self.damage = damage
        self.transform = self.owner.transform
        self.forward_dir = forward_dir
        self.transform.rotation = rotation
        self.owner.image = pygame.transform.rotate(self.owner.image, self.transform.rotation)
        
    def serialize(self):
        dt = super().serialize()
        dt.update(
            {
                'type': self.__class__.__name__,
                'damage': self.damage,
            }
        )

    @classmethod
    def deserialize(cls, d: dict) -> 'BaseProjectile':
        damage = d["damage"]
        return cls(damage)

    def update(self):
        super().update()
        self.move(0)
        
    
    def move(self, dir):
        from Scripts.Components.PhysicsComponents import Rigidbody
        rb = self.owner.get_component(Rigidbody)
        rb.add_force((self.forward_dir), self.owner)
    
    
