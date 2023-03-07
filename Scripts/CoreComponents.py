import pygame
from overrides import override
from DesignPatterns.ComponentPattern import Component
from Scripts.animation import Animation


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
    def __init__(self, owner_go, animations_list):
        super().__init__(owner_go)
        self.animations_list = animations_list
        self.current_anim = None
        self.current_frame = 0
        self.frame_timer = 0
        #for a in animations_list:
        #    sprite_sheet = pygame.image.load(a.image_path)
        #    Split the spritesheet into frames
        #    frame_width = sprite_sheet.get_width() // a.num_frames
        #    for i in range(a.num_frames):
        #        frame_rect = pygame.Rect(i * frame_width, 0, frame_width, sprite_sheet.get_height())
        #        frame_image = sprite_sheet.subsurface(frame_rect)
        #        a.frames.append(frame_image)
        #        if a.state == "idle":
        #            self.current_anim = a




    def update(self):
        # Update the frame timer
        if len(self.animations_list) <= 0:
            return
        anim = self.current_anim
        self.frame_timer += self.owner.world.delta_time

        # Check if it's time to switch to the next frame
        if self.frame_timer >= anim.frame_duration:
            self.frame_timer -= anim.frame_duration
            self.current_frame = (self.current_frame + 1) % anim.num_frames
            print(self.current_frame)



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
    def deserialize(cls, d: dict) -> 'Animator':
        animations_list = []
        for comp_data in d['animations_list']:
            animation = [Animation(comp_data["state"], comp_data["image_path"], comp_data["num_frames"], comp_data["frame_duration"])]
            animations_list.append(animation)
            print(animation[0])
        return cls(None, animations_list)
