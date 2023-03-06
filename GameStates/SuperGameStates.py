from abc import ABC, abstractmethod
import pygame.time
from DesignPatterns.StatePattern import IState


class GameState(IState, ABC):

    @abstractmethod
    def __init__(self, GameWorld, StateMachine):
        self.game_world = GameWorld
        self.stateMachine = StateMachine
        self.clock = pygame.time.Clock()
        self.delta_time = None

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def execute(self):
        self.delta_time = self.clock.tick(60) / 1000.0
        for go in self.game_world.gameobjects:
            go.update()

    @abstractmethod
    def state_transition(self):
        pass

    @abstractmethod
    def draw(self, screen):
        for obj in self.game_world.gameobjects:
            obj.draw(screen)

    @abstractmethod
    def exit(self):
        pass
