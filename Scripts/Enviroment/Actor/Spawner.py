import os

import pygame
from overrides import override
from Scripts.DesignPatterns.ComponentPattern import Component
from Scripts.Enviroment.Actor.ActorFactory import AstroidFactory, AstroidType, EnemyFactory, EnemyType
import globals


class Spawner():

    def __init__(self, game_world):
        self.world = game_world
        self.count = 1
        self.initialize_astroid(AstroidType.LargeAstroid)
        self.last_spawn_time = 0
        self.cooldown_time = 10000  # set the cooldown time in milliseconds
        self.boss_count = 0

    def initialize_astroid(self, type):
        self.world.instantiate_go(AstroidFactory().CreateProduct(AstroidType.LargeAstroid, self.world))
    def split_astroid(self, type):
        self.world.instantiate_go(AstroidFactory().CreateProduct(AstroidType.SmallAstroid, self.world))
    def spawn_enemy(self, e_type):
        self.world.instantiate_go(EnemyFactory().CreateProduct(e_type, self.world))


    # updates difficulty/stages based on player score - 4 stages
    def update(self):
        self.count += 1
        if globals.score < globals.Stages.one.value:
            if self.count % 300 == 0:
                self.initialize_astroid(AstroidType.LargeAstroid)
            if self.count % 500 == 0:
                self.split_astroid(AstroidType.SmallAstroid)
        elif globals.score < globals.Stages.two.value:
            if self.count % 250 == 0:
                self.initialize_astroid(AstroidType.LargeAstroid)
            if self.count % 300 == 0:
                self.split_astroid(AstroidType.SmallAstroid)
        elif globals.score < globals.Stages.three.value:
            if self.count % 200 == 0:
                self.initialize_astroid(AstroidType.LargeAstroid)
            if self.count % 250 == 0:
                self.split_astroid(AstroidType.SmallAstroid)
        elif globals.score < globals.Stages.four.value:
            if self.count % 150 == 0:
                self.initialize_astroid(AstroidType.LargeAstroid)
            if self.count % 200 == 0:
                self.split_astroid(AstroidType.SmallAstroid)

        current_time = pygame.time.get_ticks()
        time_since_last_spawn = current_time - self.last_spawn_time
        if time_since_last_spawn < self.cooldown_time:
            return

        # If enough time has passed, update last shot time
        self.last_spawn_time = current_time
        if self.boss_count == 2:
            self.spawn_enemy(EnemyType.BOSS)
            print("boss")
            self.boss_count = 0
        else:
            self.spawn_enemy(EnemyType.DEFAULT)
            self.boss_count += 1