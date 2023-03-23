import pygame.image
from overrides import override
import globals
from Scripts.DesignPatterns.ComponentPattern import Component


class Animation(Component):
    def __init__(self, state, image_path, num_frames, frame_duration):
        self.state = state
        self.image_path = image_path
        #self.sprite_sheet = pygame.image.load(image_path)
        self.original_image = pygame.image.load(image_path)
        self.original_width, self.original_height = self.original_image.get_size()

        self.scaled_width = int(self.original_width * globals.go_size_scale)
        self.scaled_height = int(self.original_height * globals.go_size_scale)
        self.sprite_sheet = pygame.transform.scale(self.original_image, (self.scaled_width, self.scaled_height))
        self.num_frames = num_frames
        self.frame_duration = frame_duration
        self.frames = []


        # Split the spritesheet into frames
        frame_width = self.sprite_sheet.get_width() // self.num_frames
        for i in range(self.num_frames):
            frame_rect = pygame.Rect(i * frame_width, 0, frame_width, self.sprite_sheet.get_height())
            frame_image = self.sprite_sheet.subsurface(frame_rect)
            self.frames.append(frame_image)

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
    def deserialize(cls, d: dict, owner_go) -> 'Animation':
        state = d["state"]
        image_path = d["image_path"]
        num_frames = d["num_frames"]
        frame_duration = d["frame_duration"]
        return cls(owner_go, state, image_path, num_frames, frame_duration)
