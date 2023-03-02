import pygame.image
from abc import abstractmethod, ABC
from Transform import Transform
from overrides import override


class GameObject(ABC):
    def __init__(self, x, y, image, world):
        self.transform = Transform(position=(x, y))
        self.image = pygame.image.load(image)
        self.world = world

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.transform.position)
