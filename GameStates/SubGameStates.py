import os
import pygame.font
import GameStates.SuperGameStates
from UI.UIComponents import UIButton, BackGround
from UI.UIFactory import ButtonFactory, UIProduct
from UI.UIObjects import UIObject


class MenuGameState(GameStates.SuperGameStates.GameState):
    def __init__(self, world, StateMachine):
        super().__init__(world, StateMachine)
        pygame.font.init()

    def enter(self):
        super().enter()
        _start_b_image = os.path.join(self.game_world.project_dir, "Content", "GUI", "play.png")
        _start_b_image_hover = os.path.join(self.game_world.project_dir, "Content", "GUI", "play_hover.png")
        _exit_b_image = os.path.join(self.game_world.project_dir, "Content", "GUI", "quit.png")
        _exit_b_image_hover = os.path.join(self.game_world.project_dir, "Content", "GUI", "quit_hover.png")
        _backGround_b_image = os.path.join(self.game_world.project_dir, "Content", "GUI", "spaceBackGround.png")

        a = ButtonFactory()
        self.game_world.instantiate_go(a.CreateProduct(UIProduct.StartButton))
        print()

    def execute(self):
        super().execute()

    def draw(self, screen):
        super().draw(screen)

    def state_transition(self):
        for event in pygame.event.get():
            if event.type == self.test_event:
                for obj in list(self.game_world.gameobjects):
                    self.game_world.destroy_go(obj)
                self.stateMachine.change_state(self.game_world.play_game_state)

    def exit(self):
        super().exit()


class PlayGameState(GameStates.SuperGameStates.GameState):
    def __init__(self, world, StateMachine):
        super().__init__(world, StateMachine)

    def enter(self):
        super().enter()
        self.game_world.initialize_player()

    def execute(self):
        super().execute()

    def draw(self, screen):
        super().draw(screen)

    def state_transition(self):
        pass

    def exit(self):
        super().exit()
