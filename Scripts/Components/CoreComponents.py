import pygame
from overrides import override
from Scripts.DesignPatterns.ComponentPattern import Component
from Scripts.Components.PhysicsComponents import Rigidbody
from Scripts.Components.animation import Animation


class Transform(Component):
    def __init__(self, owner_go, position=(0, 0), rotation=0, scale=(1, 1)):
        super().__init__(owner_go)
        self._position = pygame.math.Vector2(position)
        self._rotation = rotation
        self._scale = pygame.math.Vector2(scale)
        self._rect = owner_go.image.get_rect(center=position)

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
    def deserialize(cls, d: dict, owner_go) -> 'Transform':
        position = pygame.math.Vector2(d["position"][0], d["position"][1])
        rotation = d["rotation"]
        scale = pygame.math.Vector2(d["scale"][0], d["scale"][1])
        owner = owner_go
        return cls(owner, position, rotation, scale, )

    @property
    def position(self):
        return self._position

    @property
    def rect(self):
        return self._rect

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def rotation(self):

        if self._rotation > 360:
            self._rotation = self._rotation % 360
        elif self._rotation < -360:
            self._rotation = -((-self._rotation) % 360)
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = value

    @property
    def scale(self):
        return self._scale

    def translate(self, x, y):
        # Convert (x, y) tuple to a Vector2 object
        offset = pygame.math.Vector2(x, y)

        # Update the position
        self._position += offset

        self._rect.center = self._position
        return self._position

    def rotate_image(self, surf, rotate):
        self._rotation += rotate

    def scale_by(self, vectorAmount):
        self._scale *= pygame.math.Vector2(vectorAmount)


class Animator(Component):
    def __init__(self, owner_go, animations_list):
        super().__init__(owner_go)
        self.animations_list = animations_list
        self.current_anim = None
        self.current_frame = 0
        self.frame_timer = 0
        self.start = False

    def update(self):
        if self.current_anim == None:
            self.set_animation("idle")

        if self.owner.get_component(Rigidbody).velocity.magnitude() > 0.0:
            self.set_animation("boost")
        else:
            self.set_animation("idle")
        # Update the frame timer
        if self.current_anim != None:

            anim = self.current_anim

            self.frame_timer += self.owner.world.delta_time

            # Check if it's time to switch to the next frame
            if self.frame_timer >= anim.frame_duration:
                self.frame_timer -= anim.frame_duration
                self.current_frame = (self.current_frame + 1) % anim.num_frames

    def set_animation(self, state):
        for a in self.animations_list:
            if a.state == state:
                self.current_anim = a
                self.current_frame = 0

    def get_current_frame(self):
        return self.current_anim.frames[self.current_frame]

    def serialize(self):
        d = super().serialize()
        animations = [a.serialize() for a in self.animations_list]
        d.update({
            'type': self.__class__.__name__,
            'animations_list': animations,
        })
        return d

    @classmethod
    @override
    def deserialize(cls, d: dict, owner_go) -> 'Animator':
        animations_list = []
        for comp_data in d['animations_list']:
            animation = Animation(comp_data['state'], str(comp_data['image_path']), comp_data['num_frames'],
                                  comp_data['frame_duration'])
            animations_list.append(animation)

        cls.animations_list = animations_list

        return cls(owner_go, animations_list)
