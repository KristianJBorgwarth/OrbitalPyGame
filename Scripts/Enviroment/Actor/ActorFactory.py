import os
import random

import globals
from enum import Enum
from Scripts.DesignPatterns.FactoryPattern import AbstractFactory
from Scripts.Core.GameObject import GameObject, Layers


class AstroidType(Enum):
    SmallAstroid = 1
    LargeAstroid = 2
    SplitAstroid = 3


class AstroidFactory(AbstractFactory):
    def __init__(self):
        self.x = None
        self.y = None
        self.ranPoint = None

    def CreateProduct(self, enum: AstroidType, game_world, offset=(0, 0)) -> GameObject:
        from Scripts.Core.GameObjectCreator import GameObjectFactory, GameObjectBuilder
        if enum is AstroidType.SmallAstroid:
            img_path = os.path.join(globals.project_path, "Content", "Astroid", "astroid_small.png")
            img_width = 16
            img_height = 16

            self.ranPoint = random.choice(
                [(random.randrange(0, 1920 - img_width), random.choice([-1 * img_width - 5, 1080 + 5])),
                 (random.choice([-1 * img_width - 5, 1920 + 5]), random.randrange(0, 1080 - img_height))])

            self.x, self.y = self.ranPoint

            
            asteroid_go = GameObjectFactory.build_base(x=self.x, y=self.y, image_path=img_path, world=game_world,
                                                       layer=Layers.FOREGROUND, tag="Asteroid_Small")

            GameObjectBuilder.add_astroid_small(asteroid_go)

        if enum is AstroidType.LargeAstroid:
            img_path = os.path.join(globals.project_path, "Content", "Astroid", "astroid_large.png")
            img_width = 117
            img_height = 109

            self.ranPoint = random.choice(
                [(random.randrange(0, 1920 - img_width), random.choice([-1 * img_width - 5, 1080 + 5])),
                 (random.choice([-1 * img_width - 5, 1920 + 5]), random.randrange(0, 1080 - img_height))])

            self.x, self.y = self.ranPoint
            
            asteroid_go = GameObjectFactory.build_base(x=self.x, y=self.y, image_path=img_path, world=game_world,
                                                       layer=Layers.FOREGROUND, tag="Asteroid_Large")
            GameObjectBuilder.add_astroid_large(asteroid_go)

        if enum is AstroidType.SplitAstroid:
            img_path = os.path.join(globals.project_path, "Content", "Astroid", "astroid_small.png")
            img_width = 16
            img_height = 16

            if offset[0] is not 0 and offset[1] is not 0:
                self.x = offset[0]
                self.y = offset[1]

            print(self.x, self.y)
            asteroid_go = GameObjectFactory.build_base(x=self.x, y=self.y, image_path=img_path, world=game_world,
                                                       layer=Layers.FOREGROUND, tag="Asteroid_Split")

            GameObjectBuilder.add_astroid_split(asteroid_go)
            globals.astroidCount += 1
        GameObjectBuilder.add_collision_handler(asteroid_go)
        
        # Add Collision rules here
        # asteroid_go.add_collision_rule("Player")
        
        return asteroid_go

    
