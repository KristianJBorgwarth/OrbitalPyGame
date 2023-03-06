import pygame.math
from abc import ABC, abstractmethod
from overrides import override
import GameObject


class Component(ABC):
    def __init__(self, owner_go: GameObject):
        self.owner = owner_go

    def update(self):
        pass

    @abstractmethod
    def serialize(self):
        return {'type': self.__class__.__name__}

    @classmethod
    @abstractmethod
    def deserialize(cls, d: dict) -> 'Component':
        pass


class Rigidbody(Component):

    def __init__(self, acceleration, friction, max_speed, owner_go: GameObject):
        super().__init__(owner_go)
        self.acceleration = pygame.math.Vector2(acceleration)  # set the acceleration to a certain value
        self.friction = pygame.math.Vector2(friction)  # set the friction to a certain value
        self.max_speed = pygame.math.Vector2(max_speed)  # set the maximum speed to a certain value
        self._velocity = pygame.math.Vector2(0, 0)  # initialize the velocity to zero

    def serialize(self):
        dt = super().serialize()
        dt.update({
            'type': self.__class__.__name__,
            'acceleration': list(self.acceleration),
            'friction': list(self.friction),
            'max_speed': list(self.max_speed),
            'velocity': list(self._velocity),
        })
        return dt

    @classmethod
    @override
    def deserialize(cls, d: dict) -> 'Rigidbody':
        acceleration = pygame.math.Vector2(d["acceleration"])
        friction = pygame.math.Vector2(d["friction"])
        max_speed = pygame.math.Vector2(d["max_speed"])
        velocity = pygame.math.Vector2(d["velocity"])
        return cls(acceleration, friction, max_speed, velocity)

    @property
    def velocity(self):
        return self._velocity

    @override
    def update(self):
        super().update()

    def update_velocity(self, axis, delta_time, keys, directions):
        # Get the current velocity, acceleration, max speed, and friction for the given axis
        velocity = getattr(self._velocity, axis)
        acceleration = getattr(self.acceleration, axis)
        max_speed = getattr(self.max_speed, axis)
        friction = getattr(self.friction, axis)

        # Update the velocity based on user input and acceleration
        if keys[directions[axis]['positive']]:
            velocity = min(velocity + acceleration * delta_time, max_speed)
        elif keys[directions[axis]['negative']]:
            velocity = max(velocity - acceleration * delta_time, -max_speed)
        else:
            # Apply friction if no input is given
            friction_force = friction * delta_time
            velocity = max(0, abs(velocity) - friction_force) * (1 if velocity > 0 else -1)

        # Set the updated velocity for the given axis
        setattr(self._velocity, axis, velocity)


class Transform(Component):
    def __init__(self, owner_go: GameObject, position=(0, 0), rotation=0, scale=(1, 1)):
        super().__init__(owner_go)
        self._position = pygame.math.Vector2(position)
        self._rotation = rotation
        self._scale = pygame.math.Vector2(scale)

    def serialize(self):
        d = super().serialize()
        d.update({
            'type': self.__class__.__name__,
            'position': list(self.position),
            'rotation': self._rotation,
            'scale': list(self.scale),
        })
        return d

    @classmethod
    @override
    def deserialize(cls, d: dict) -> 'Transform':
        position = pygame.math.Vector2(d["position"][0], d["position"][1])
        rotation = d["rotation"]
        scale = pygame.math.Vector2(d["scale"][0], d["scale"][1])
        return cls(None, position, rotation, scale)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def rotation(self):
        return self._rotation

    @property
    def scale(self):
        return self._scale

    def translate(self, x, y):
        self._position += pygame.math.Vector2(x, y)

    def rotate(self, angleAmount):
        self._rotation = (self._rotation + angleAmount) % 360

    def scale_by(self, vectorAmount):
        self._scale *= pygame.math.Vector2(vectorAmount)


class Player(Component):
    def __init__(self, owner_go: GameObject):
        super().__init__(owner_go)

        self.owner = owner_go
        self.rigidbody = self.owner.get_component(Rigidbody)

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
    def deserialize(cls, d: dict) -> 'Component':
        pass

    @override
    def update(self):
        super().update()
        keys = pygame.key.get_pressed()

        # Quit on escape
        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        if self.rigidbody is None:
            return

        self.rigidbody.update_velocity('x', self.owner.world.delta_time, keys, self.directions)
        self.rigidbody.update_velocity('y', self.owner.world.delta_time, keys, self.directions)

        # update the position based on velocity
        self.owner.transform.translate(*self.rigidbody.velocity * self.owner.world.delta_time)

        if self.rigidbody.velocity.magnitude() > 0.0:
            print(f"Velocity > x: {self.rigidbody.velocity.x.__round__()}, y: {self.rigidbody.velocity.y.__round__()}")
