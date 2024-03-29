﻿import pygame
from typing import Any

import globals
from Scripts.DesignPatterns.ComponentPattern import Component
from Scripts.DesignPatterns.BehaviourPattern import Behaviour


class Enemy(Component):
    def __init__(self, owner_go):
        super().__init__(owner_go)
        self.behaviours = []
        self.health = 3

    def update(self):
        super().update()
        for behaviour in self.behaviours:
            behaviour.update()

    def serialize(self):
        return super().serialize()

    @classmethod
    def deserialize(cls, d: dict, owner_go) -> Any:
        return super().deserialize(d, owner_go)

    def add_behaviour(self, behaviour: Behaviour):
        if behaviour in self.behaviours:
            return
        self.behaviours.append(behaviour)

    def remove_behaviour(self, behaviour: Behaviour):
        if behaviour in self.behaviours:
            self.behaviours.remove(behaviour)

    def on_take_damage(self):
        self.health -= 1
        if self.health <= 0:
            globals.score += 30
            self.owner.world.destroy_go(self.owner)
