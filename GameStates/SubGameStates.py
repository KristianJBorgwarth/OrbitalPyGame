import pygame.font
import GameStates.SuperGameStates
from UI.UIFactory import ButtonFactory, UIProduct, BackGroundFactory, UIBackground
from Enviroment.Actor.ActorFactory import AstroidFactory, AstroidType
from Enviroment.Actor.Spawner import Spawner
from HighscoreManager.highscoremanager import HighScoreManager
import globals


class MenuGameState(GameStates.SuperGameStates.GameState):
    def __init__(self, world, StateMachine):
        super().__init__(world, StateMachine)
        globals.highscore_manager = HighScoreManager()
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
        self.game_world.initialize_player()
        self.spawner = Spawner(self.game_world)

    def execute(self):
        super().execute()
        self.spawner.update()
        globals.highscore_manager.update_high_score()
        globals.levelManager.update_level()

    def draw(self, screen):
        super().draw(screen)
        globals.fontManager.render_font(f"Score:{globals.score}", (50, 100), screen, "white")
        globals.fontManager.render_font(f"Level:{globals.level}", (globals.width - globals.fontManager.get_text_width(f"Level:{globals.score}") - 25, 50), screen, "white")
        globals.fontManager.render_font(f"High Score:{globals.high_score}", (50, 50), screen, "white")


    def state_transition(self):
        pass

    def exit(self):
        super().exit()


class GameOverState(GameStates.SuperGameStates.GameState):
    def __init__(self, world, StateMachine):
        super().__init__(world, StateMachine)

    def enter(self):
        globals.highscore_manager.add_score("Martin")
        globals.highscore_manager.save_leaderboard()
        globals.highscore_manager.reset_score()
        pass

    def execute(self):
        pass

    def state_transition(self):
        pass

    def draw(self, screen):
        pass

    def exit(self):
        pass
