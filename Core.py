import pygame
from GameStates.SubGameStates import PlayGameState, MenuGameState
from DesignPatterns.StatePattern import StateMachine


class GameWorld:
    def __init__(self, width, height, caption):
        pygame.font.init()
        self.StateMachine = None
        self.playGameState = PlayGameState(self, self.StateMachine)
        self.menuGameState = MenuGameState(self, self.StateMachine)
        self.gameobjects = []
        self.width = width
        self.height = height
        self.caption = caption
        self.gameobjects = []
        self.clock = pygame.time.Clock()
        self.delta_time = None

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)
        self.setup_state_logic()

    def instantiate_go(self, go):
        self.gameobjects.append(go)

    def update(self):
        self.StateMachine.currentState.execute()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.StateMachine.currentState.draw(self.screen)
        pygame.display.flip()

    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update()
            self.draw()

        pygame.quit()

    def setup_state_logic(self):
        self.StateMachine = StateMachine(self.menuGameState)
