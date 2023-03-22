import os
import pygame.font
import GameStates.SuperGameStates
from UI.UIFactory import ButtonFactory, UIProduct, BackGroundFactory, UIBackground
from Scripts.Spawner import Spawner
import globals


class MenuGameState(GameStates.SuperGameStates.GameState):
    def __init__(self, world, StateMachine):
        super().__init__(world, StateMachine)
        pygame.font.init()

    def enter(self):
        super().enter()
        self.game_world.instantiate_go(BackGroundFactory().CreateProduct(UIBackground.MenuBackGround, self.game_world))
        self.game_world.instantiate_go(ButtonFactory().CreateProduct(UIProduct.StartButton, self.game_world))
        self.game_world.instantiate_go(ButtonFactory().CreateProduct(UIProduct.ExitButton, self.game_world))

    def execute(self):
        super().execute()

    def draw(self, screen):
        super().draw(screen)

    def state_transition(self):
        for event in pygame.event.get():
            if event.type == globals.start_event:
                for obj in list(self.game_world.gameobjects):
                    self.game_world.destroy_go(obj)
                self.stateMachine.change_state(self.game_world.play_game_state)
            elif event.type == globals.quit_event:
                pygame.quit()

    def exit(self):
        super().exit()


class PlayGameState(GameStates.SuperGameStates.GameState):
    def __init__(self, world, StateMachine):
        super().__init__(world, StateMachine)

    def enter(self):
        super().enter()
        self.game_world.instantiate_go(BackGroundFactory().CreateProduct(UIBackground.EasyDiffBackground, self.game_world))
        self.game_world.initialize_player()
        Spawner(self.game_world)

    def execute(self):
        super().execute()

    def draw(self, screen):
        super().draw(screen)
        globals.fontManager.render_font(f"Score:{globals.score}", (50, 50), screen, "black")

    def state_transition(self):
        pass

    def exit(self):
        super().exit()


class GameOverState(GameStates.SuperGameStates.GameState):
    def __init__(self, world, StateMachine):
        super().__init__(world, StateMachine)

    def enter(self):
        self.game_world.instantiate_go(BackGroundFactory().CreateProduct(UIBackground.GameOverBackground, self.game_world))

    def execute(self):
        super().execute()

    def state_transition(self):
        super().state_transition()

    def draw(self, screen):
        super().draw(screen)

    def exit(self):
        super().exit()