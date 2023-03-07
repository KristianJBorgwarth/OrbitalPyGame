import pygame.image
from overrides import override

from DesignPatterns.ComponentPattern import Component


class Animation(Component):
    def __init__(self, state, image_path, num_frames, frame_duration):
        self.state = state
        self.image_path = image_path
        self.sprite_sheet = pygame.image.load(image_path)
        self.num_frames = num_frames
        self.frame_duration = frame_duration
        self.frames = []
    def __str__(self):
        return f"{self.state}, {self.image_path}, {self.num_frames}, {self.frame_duration}"
    def serialize(self):
        d = super().serialize()
        d.update({
            'type': self.__class__.__name__,
            'state': self.state,
            'image_path': self.image_path,
            'num_frames': self.num_frames,
            'frame_duration': self.frame_duration,
        })
        return d

    @classmethod
    @override
    def deserialize(cls, d: dict) -> 'Animation':
        state = d["state"]
        image_path = d["image_path"]
        num_frames = d["num_frames"]
        frame_duration = d["frame_duration"]
        return cls(None, state, image_path, num_frames, frame_duration)

