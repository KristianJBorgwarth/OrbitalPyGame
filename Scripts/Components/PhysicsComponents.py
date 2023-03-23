import pygame
from overrides import override

from Scripts.DesignPatterns.ComponentPattern import Component


class Rigidbody(Component):

    def __init__(self, acceleration, friction, max_speed, owner_go):
        super().__init__(owner_go)
        self.owner = owner_go
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
    def deserialize(cls, d: dict, owner_go) -> 'Rigidbody':
        acceleration = pygame.math.Vector2(d["acceleration"])
        friction = pygame.math.Vector2(d["friction"])
        max_speed = pygame.math.Vector2(d["max_speed"])
        owner = owner_go
        return cls(acceleration, friction, max_speed, owner)

    @property
    def velocity(self):
        return self._velocity

    @override
    def update(self):


        super().update()

    def add_force(self, direction, go):
        # Convert direction to a vector and normalize it
        force_direction = pygame.math.Vector2(direction).normalize()
    
        # Calculate the force based on acceleration and elapsed time
        force = self.acceleration * self.owner.world.delta_time
        force.x *= force_direction.x
        force.y *= force_direction.y
    
        # Update the velocity with the force
        self._velocity += force
    
        # Cap the velocity using the max speed
        if self._velocity.length() > self.max_speed.length():
            self._velocity = self._velocity.normalize() * self.max_speed.length()
    
        # Translate the game object based on the updated velocity and elapsed time
        go.transform.translate(*(self.velocity * self.owner.world.delta_time))
            
    def update_velocity(self, axis, keys, directions, go, forward_dir):
        # Get the current velocity, acceleration, max speed, and friction for the given axis
        velocity = getattr(self._velocity, axis)
        acceleration = getattr(self.acceleration, axis)
        max_speed = getattr(self.max_speed, axis)
        friction = getattr(self.friction, axis)
    
        # Update the velocity based on user input and acceleration
        if keys[directions[axis]['positive']]:
            velocity = min(velocity + acceleration * self.owner.world.delta_time, max_speed)
        elif keys[directions[axis]['negative']]:
            velocity = max(velocity - acceleration * self.owner.world.delta_time, -max_speed)
        else:
            # Apply friction if no input is given
            friction_force = friction * self.owner.world.delta_time
            velocity = max(0, abs(velocity) - friction_force) * (1 if velocity > 0 else -1)
    
        # Set the updated velocity for the given axis
        setattr(self._velocity, axis, velocity)
    
        # Check if the forward direction vector has a length of zero
        if forward_dir.length() == 0:
            # If it does, move the game object in the direction of the velocity vector
            target_dir = self.velocity.normalize()
        else:
            # Multiply the velocity vector with the forward direction vector to get the velocity in the forward direction
            target_dir = forward_dir.normalize() * velocity
    
        # Translate the player's position using the target direction and the delta time
        translation = target_dir * self.owner.world.delta_time
        
        go.transform.translate(translation.x, translation.y)


