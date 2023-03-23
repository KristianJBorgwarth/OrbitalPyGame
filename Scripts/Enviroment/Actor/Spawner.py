import os
from overrides import override
from Scripts.DesignPatterns.ComponentPattern import Component
from Scripts.Enviroment.Actor.ActorFactory import AstroidFactory, AstroidType
import globals


class Spawner():

    def __init__(self, game_world):
        self.world = game_world
        self.count = 1
        self.initialize_astroid(AstroidType.LargeAstroid)

    def initialize_astroid(self, type):
        self.world.instantiate_go(AstroidFactory().CreateProduct(AstroidType.LargeAstroid, self.world))
    def split_astroid(self, type):
        self.world.instantiate_go(AstroidFactory().CreateProduct(AstroidType.SmallAstroid, self.world))

    # updates difficulty/stages based on player score - 4 stages
    def update(self):
        self.count += 1
        if globals.score < globals.Stages.one.value:
            if self.count % 300 == 0:
                self.initialize_astroid(AstroidType.LargeAstroid)
            if self.count % 500 == 0:
                self.split_astroid(AstroidType.SmallAstroid)
        elif globals.score < globals.Stages.two.value:
            if self.count % 150 == 0:
                self.initialize_astroid(AstroidType.LargeAstroid)
            if self.count % 250 == 0:
                self.split_astroid(AstroidType.SmallAstroid)
        elif globals.score < globals.Stages.three.value:
            if self.count % 75 == 0:
                self.initialize_astroid(AstroidType.LargeAstroid)
            if self.count % 125 == 0:
                self.split_astroid(AstroidType.SmallAstroid)
        elif globals.score < globals.Stages.four.value:
            if self.count % 75 == 0:
                self.initialize_astroid(AstroidType.LargeAstroid)
            if self.count % 125 == 0:
                self.split_astroid(AstroidType.SmallAstroid)

