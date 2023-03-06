from Components import Component
from Scripts import GameObject


class BaseProjectile(Component):
    def __init__(self, owner_go: GameObject, damage, speed):
        super().__init__(owner_go)
        self.damage = damage
        self.speed = speed
        self.transform = self.owner.transform

    def serialize(self):
        dt = super().serialize()
        dt.update(
            {
                'type': self.__class__.__name__,
                'damage': self.damage,
                'speed': self.speed
            }
        )

    @classmethod
    def deserialize(cls, d: dict) -> 'BaseProjectile':
        damage = d["damage"]
        speed = d["speed"]
        return cls(damage, speed)

    def update(self):
        super().update()
        
    
    
