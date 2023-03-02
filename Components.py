import pygame.math


class Rigidbody:
    def __init__(self, acceleration, friction, max_speed):
        self.acceleration = pygame.math.Vector2(acceleration)  # set the acceleration to a certain value
        self.friction = pygame.math.Vector2(friction)  # set the friction to a certain value
        self.max_speed = pygame.math.Vector2(max_speed)  # set the maximum speed to a certain value
        self._velocity = pygame.math.Vector2(0, 0)  # initialize the velocity to zero

    @property
    def velocity(self):
        return self._velocity

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

