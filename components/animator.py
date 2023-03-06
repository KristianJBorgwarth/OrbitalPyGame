import os
import pygame
from overrides import override
from Scripts.Components import Component



class Animator(Component):
    def __init__(self, image_folder, frame_duration, world):
        self.world = world
        self.image_folder = image_folder
        self.frame_duration = frame_duration
        self.frames = []
        self.current_frame = 0
        self.frame_timer = 0


    def update_images(self, image_folder):
        # Load the frames from the image folder
        frames = []
        for filename in os.listdir(image_folder):
            if filename.endswith(".png"):
                image_path = os.path.join(image_folder, filename)
                frame_image = pygame.image.load(image_path).convert_alpha()
                frames.append(frame_image)
        self.frames = frames
    def update(self):
        self.update_images(self.image_folder)
        # Update the frame timer
        self.frame_timer += self.world.delta_time

        # Check if it's time to switch to the next frame
        if self.frame_timer >= self.frame_duration:
            self.frame_timer -= self.frame_duration
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def get_current_frame(self):
        return self.frames[self.current_frame]

    def serialize(self):
        pass

    @classmethod
    @override
    def deserialize(cls, d: dict) -> 'Transform':
        pass