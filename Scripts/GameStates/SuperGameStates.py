from abc import ABC, abstractmethod
import pygame.time
from Scripts.DesignPatterns.StatePattern import IState


class GameState(IState, ABC):

    @abstractmethod
    def __init__(self, world, StateMachine):
        self.game_world = world
        self.stateMachine = StateMachine
        self.clock = pygame.time.Clock()
        self.delta_time = None

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def execute(self):
        self.game_world.delta_time = self.clock.tick(60) / 1000.0
        for go in self.game_world.gameobjects:
            go.update()
        self._handle_collisions()
        self.game_world.clear_removed_objects()

    @abstractmethod
    def state_transition(self):
        pass

    @abstractmethod
    def draw(self, screen):
        for go in self.game_world.gameobjects:
            go.draw(screen)

        for layer in self.game_world.render_layers:
            for go in layer:
                from Scripts.Core.GameObject import GameObject
                if isinstance(go, GameObject):
                    go.draw(screen)
                    if go.get_image_rect() is not None:
                        pygame.draw.rect(surface=screen, color=go.collision_color,
                                        rect=go.get_image_rect(), width=3)
                else:
                    go.draw(screen)

    @abstractmethod
    def exit(self):
        pass

    def _handle_collisions(self):
        from Scripts.Core.GameObject import GameObject
        # Handle collision between two gameobjects
        for go1 in self.game_world.gameobjects:
            for go2 in self.game_world.gameobjects:
                if isinstance(go1, GameObject) and isinstance(go2, GameObject):
                    if go1 != go2:
                        if go1.transform.rect.colliderect(go2.transform.rect):
                            if (go1, go2) not in self.game_world.colliding_gameobjects:
                                # Objects have just started colliding
                                go1.handle_collision(go2, "enter")
                                go2.handle_collision(go1, "enter")
                                self.game_world.colliding_gameobjects.append((go1, go2))
                            else:
                                # Objects are still colliding
                                go1.handle_collision(go2, "stay")
                                go2.handle_collision(go1, "stay")
                        elif (go1, go2) in self.game_world.colliding_gameobjects:
                            # Objects have stopped colliding
                            go1.handle_collision(go2, "exit")
                            go2.handle_collision(go1, "exit")
                            self.game_world.colliding_gameobjects.remove((go1, go2))
