import os
from overrides import override
from Scripts.DesignPatterns.ComponentPattern import Component
from Scripts.Enviroment.Actor.ActorFactory import AstroidFactory, AstroidType, EnemyFactory
import globals
from Scripts.Extensions.ExtensionsEnum import EnemyType


class Spawner():

    def __init__(self, game_world):
        self.world = game_world
        self.count = 1
        self.astroidCount = 0
        self.initialize_astroid(AstroidType.LARGE)
        self.spawn_enemy(EnemyType.DEFAULT)

    def initialize_astroid(self, type):
        self.world.instantiate_go(AstroidFactory().CreateProduct(AstroidType.LARGE, self.world))
        globals.astroidCount += 1

    def split_astroid(self, type):
        self.world.instantiate_go(AstroidFactory().CreateProduct(AstroidType.SMALL, self.world))
        globals.astroidCount += 1

    def spawn_enemy(self, e_type: EnemyType):
        self.world.instantiate_go(EnemyFactory().CreateProduct(e_type, self.world))

    def update(self):
        self.count += 1
        if self.count % 300 == 0:
            self.initialize_astroid(AstroidType.LARGE)

        if self.count % 500 == 0:
            self.split_astroid(AstroidType.SMALL)
