import GameStates.SuperGameStates
from MenuLogic.Button import Button
from Enviroment.Backgrounds import MenuBackground
from MenuLogic.ButtonCommands import StartGameCommand, ExitGameCommand


class MenuGameState(GameStates.SuperGameStates.GameState):
    def __init__(self, world, StateMachine):
        super().__init__(world, StateMachine)

    def enter(self):
        super().enter()
        start_game_cmd = StartGameCommand()
        exit_game_cmd = ExitGameCommand()
        start_button = Button(725, 350, "Content\GUI\playButton.png", self, "PLAY", start_game_cmd)
        exit_button = Button(725, 650, "Content\GUI\playButton.png", self, "EXIT", exit_game_cmd)
        score_button = Button(725, 500, "Content\GUI\playButton.png", self, "HIGHSCORE", exit_game_cmd)
        back_ground = MenuBackground(0, 0, "Content\GUI\spaceBackground.png", self)
        self.game_world.instantiate_go(back_ground)
        self.game_world.instantiate_go(exit_button)
        self.game_world.instantiate_go(start_button)
        self.game_world.instantiate_go(score_button)

    def execute(self):
        super().execute()

    def draw(self, screen):
        super().draw(screen)

    def state_transition(self):
        pass

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
