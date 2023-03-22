import os
from overrides import override
from DesignPatterns.ComponentPattern import Component
from Enviroment.Actor.ActorFactory import AstroidFactory, AstroidType
import globals

class Spawner():

    def __init__(self, game_world):
        self.world = game_world
        self.count = 1
        self.astroidCount = 0
        self.initialize_astroid(AstroidType.LargeAstroid)

    def initialize_astroid(self, type):
        self.world.instantiate_go(AstroidFactory().CreateProduct(AstroidType.LargeAstroid, self.world))
        globals.astroidCount += 1
    def split_astroid(self, type):
        self.world.instantiate_go(AstroidFactory().CreateProduct(AstroidType.SmallAstroid, self.world))
        globals.astroidCount += 1

    def update(self):
        self.count += 1
        if self.count % 300 == 0:
            self.initialize_astroid(AstroidType.LargeAstroid)

        if self.count % 500 == 0:
            self.split_astroid(AstroidType.SmallAstroid)

