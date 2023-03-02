import pygame.key
from overrides import override

from GameObject import GameObject
from Components import Rigidbody


class Player(GameObject):
    def __init__(self, x, y, image, world):
        super().__init__(x, y, image, world)
        self.rigidbody = Rigidbody(acceleration=(350, 150), friction=(200, 200), max_speed=(350, 250))

        self.directions = \
            {
                'x': {'positive': pygame.K_RIGHT, 'negative': pygame.K_LEFT},
                'y': {'positive': pygame.K_DOWN, 'negative': pygame.K_UP},
            }

    @override
    def update(self):
        super().update()
        keys = pygame.key.get_pressed()

        self.rigidbody.update_velocity('x', self.world.delta_time, keys, self.directions)
        self.rigidbody.update_velocity('y', self.world.delta_time, keys, self.directions)

        # update the position based on velocity
        self.transform.translate(*self.rigidbody.velocity * self.world.delta_time)

        if self.rigidbody.velocity.magnitude() > 0.0:
            print(f"Velocity > x: {self.rigidbody.velocity.x.__round__()}, y: {self.rigidbody.velocity.y.__round__()}")
