import pygame
from overrides import override
from DesignPatterns.ComponentPattern import Component


class Transform(Component):
    def __init__(self, owner_go, position=(0, 0), rotation=0, scale=(1, 1)):
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


class Animator(Component):
    def __init__(self, sprite_sheet, num_frames, frame_duration, owner_go):
        super().__init__(owner_go)
        self.sprite_sheet = pygame.image.load(sprite_sheet)
        self.num_frames = num_frames
        self.frame_duration = frame_duration
        self.frames = []
        self.current_frame = 0
        self.frame_timer = 0
        # Split the spritesheet into frames
        frame_width = self.sprite_sheet.get_width() // self.num_frames
        for i in range(self.num_frames):
            frame_rect = pygame.Rect(i * frame_width, 0, frame_width, self.sprite_sheet.get_height())
            frame_image = self.sprite_sheet.subsurface(frame_rect)
            self.frames.append(frame_image)

    def update(self):
        # Update the frame timer
        self.frame_timer += self.owner.world.delta_time

        # Check if it's time to switch to the next frame
        if self.frame_timer >= self.frame_duration:
            self.frame_timer -= self.frame_duration
            self.current_frame = (self.current_frame + 1) % self.num_frames
    def get_current_frame(self):
        return self.frames[self.current_frame]



    def serialize(self):
        pass


    def deserialize(cls, d: dict) -> 'Animator':
        pass