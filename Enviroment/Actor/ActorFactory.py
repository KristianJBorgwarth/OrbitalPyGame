import os
import random

import globals
from enum import Enum
from DesignPatterns.FactoryPattern import AbstractFactory
from Enviroment.Actor import AstroidComponent
from Enviroment.Actor.AstroidComponent import Astroid
from Scripts.GameObject import GameObject


class AstroidType(Enum):
    SmallAstroid = 1
    LargeAstroid = 2


class AstroidFactory(AbstractFactory):
    def __init__(self, owner_go: GameObject):
        self.x = None
        self.y = None
        self.ranPoint = None
        self.owner = owner_go


    def CreateProduct(self, enum: AstroidType, game_world) -> GameObject:
        if enum is AstroidType.SmallAstroid:
            img_path = os.path.join(globals.project_path, "Content", "Astroid", "astroid_small.png")
            img_width = 16
            img_height = 16

            self.ranPoint = random.choice(
                [(random.randrange(0, 1920 - img_width), random.choice([-1 * img_width - 5, 1080 + 5])),
                 (random.choice([-1 * img_width - 5, 1920 + 5]), random.randrange(0, 1080 - img_height))])

            self.x, self.y = self.ranPoint
            astroid_go = GameObject(self.x, self.y, img_path, game_world)
            astroid_go.add_component(Astroid(astroid_go))
            self.owner.tag = "SmallAstroid"
            return astroid_go
        if enum is AstroidType.LargeAstroid:
            img_path = os.path.join(globals.project_path, "Content", "Astroid", "astroid_large.png")
            img_width = 117
            img_height = 109

            self.ranPoint = random.choice(
                [(random.randrange(0, 1920 - img_width), random.choice([-1 * img_width - 5, 1080 + 5])),
                 (random.choice([-1 * img_width - 5, 1920 + 5]), random.randrange(0, 1080 - img_height))])

            self.x, self.y = self.ranPoint
            astroid_go = GameObject(self.x, self.y, img_path, game_world)
            astroid_go.add_component(Astroid(astroid_go))
            self.owner.tag = "LargeAstroid"
            return astroid_go
