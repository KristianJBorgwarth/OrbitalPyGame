import pygame.font
import Scripts.GameStates.SuperGameStates
from Scripts.UI.UIFactory import ButtonFactory, UIButtonProduct, BackGroundFactory, UIBackground, UIDecorProduct, \
    UIDecorFactory, UITextBoxFactory, UITextBoxProduct
from Scripts.Enviroment.Actor.Spawner import Spawner
import globals


class MenuGameState(Scripts.GameStates.SuperGameStates.GameState):
    def __init__(self, world, StateMachine):
        super().__init__(world, StateMachine)
        pygame.font.init()

    def enter(self):
        super().enter()
        self.game_world.instantiate_go(BackGroundFactory().CreateProduct(UIBackground.MenuBackGround, self.game_world))
        self.game_world.instantiate_go(ButtonFactory().CreateProduct(UIButtonProduct.StartButton, self.game_world))
        self.game_world.instantiate_go(ButtonFactory().CreateProduct(UIButtonProduct.ExitButton, self.game_world))
        self.game_world.instantiate_go(ButtonFactory().CreateProduct(UIButtonProduct.HighScoreButton, self.game_world))
        self.game_world.instantiate_go(ButtonFactory().CreateProduct(UIButtonProduct.ControlsButton, self.game_world))

    def execute(self):
        super().execute()

    def draw(self, screen):
        super().draw(screen)

    def state_transition(self):
        for event in self.game_world.list_of_events:
            if event.type == globals.start_event:
                self.stateMachine.change_state(self.game_world.play_game_state)
            elif event.type == globals.highscore_event:
                self.stateMachine.change_state(self.game_world.highscore_game_state)
            elif event.type == globals.controls_event:
                self.stateMachine.change_state(self.game_world.controls_game_state)
            elif event.type == globals.quit_event:
                pygame.quit()

    def exit(self):
        super().exit()
        pygame.event.clear()
        self.game_world.destroy_all_go()


class PlayGameState(Scripts.GameStates.SuperGameStates.GameState):
    def __init__(self, world, StateMachine):
        super().__init__(world, StateMachine)

    def enter(self):
        super().enter()
        self.game_world.instantiate_go(
            BackGroundFactory().CreateProduct(UIBackground.EasyDiffBackground, self.game_world))
        self.game_world.initialize_player()
        self.spawner = Spawner(self.game_world)

    def execute(self):
        super().execute()
        self.spawner.update()

    def draw(self, screen):
        super().draw(screen)
        globals.fontManager.render_font(f"Score:{globals.score}", (50, 50), screen, "black")
        globals.fontManager.render_font(f"Astroids:{globals.astroidCount}", (50, 100), screen, "black")

    def state_transition(self):
        if globals.player_is_dead is True:
            for obj in self.game_world.gameobjects:
                obj.on_disable()
            self.stateMachine.change_state(self.game_world.game_over_game_state)

    def exit(self):
        super().exit()


class GameOverState(Scripts.GameStates.SuperGameStates.GameState):
    def __init__(self, world, StateMachine):
        super().__init__(world, StateMachine)

    def enter(self):
        self.game_world.instantiate_go(BackGroundFactory().CreateProduct(UIBackground.GameOverBackground, self.game_world))
        self.game_world.instantiate_go(ButtonFactory().CreateProduct(UIButtonProduct.PlayAgainButton, self.game_world))
        self.game_world.instantiate_go(ButtonFactory().CreateProduct(UIButtonProduct.BackButton, self.game_world))
        self.game_world.instantiate_go(UIDecorFactory().CreateProduct(UIDecorProduct.GameOverText, self.game_world))
        self.game_world.instantiate_go(UIDecorFactory().CreateProduct(UIDecorProduct.HighScoreText, self.game_world))
        self.game_world.instantiate_go(UITextBoxFactory().CreateProduct(UITextBoxProduct.HighscoreName, self.game_world))

    def execute(self):
        super().execute()

    def state_transition(self):
        super().state_transition()
        for event in self.game_world.list_of_events:
            if event.type == globals.play_again_event:
                self.stateMachine.change_state(self.game_world.play_game_state)
            elif event.type == globals.back_event:
                self.stateMachine.change_state(self.game_world.menu_game_state)

    def draw(self, screen):
        super().draw(screen)

    def exit(self):
        super().exit()
        self.game_world.destroy_all_go()


class HighScoreMenuState(Scripts.GameStates.SuperGameStates.GameState):
    def __init__(self, world, StateMachine):
        super().__init__(world, StateMachine)

    def enter(self):
        self.game_world.instantiate_go(BackGroundFactory().CreateProduct(UIBackground.MenuBackGround, self.game_world))
        self.game_world.instantiate_go(ButtonFactory().CreateProduct(UIButtonProduct.BackButton, self.game_world))

    def execute(self):
        super().execute()

    def state_transition(self):
        for event in self.game_world.list_of_events:
            if event.type == globals.back_event:
                self.stateMachine.change_state(self.game_world.menu_game_state)

    def draw(self, screen):
        super().draw(screen)

    def exit(self):
        super().exit()
        self.game_world.destroy_all_go()


class ControlMenuState(Scripts.GameStates.SuperGameStates.GameState):
    def __init__(self, world, StateMachine):
        super().__init__(world, StateMachine)

    def enter(self):
        self.game_world.instantiate_go(BackGroundFactory().CreateProduct(UIBackground.MenuBackGround, self.game_world))
        self.game_world.instantiate_go(ButtonFactory().CreateProduct(UIButtonProduct.BackButton, self.game_world))
        self.game_world.instantiate_go(UIDecorFactory().CreateProduct(UIDecorProduct.ControlsText, self.game_world))

    def execute(self):
        super().execute()

    def state_transition(self):
        for event in self.game_world.list_of_events:
            if event.type == globals.back_event:
                self.stateMachine.change_state(self.game_world.menu_game_state)

    def draw(self, screen):
        super().draw(screen)

    def exit(self):
        super().exit()
        self.game_world.destroy_all_go()
