import pygame
from GO_Player import Player
from GO_Enemy import Enemy


class GameWorld:
    def __init__(self, width, height, caption):
        self.width = width
        self.height = height
        self.caption = caption
        self.gameobjects = []
        self.clock = pygame.time.Clock()
        self.delta_time = None

        player = Player(300, 400, "Content\Player\player.png", self)
        enemy = Enemy(600, 400, "Content\Enemy\Ship1.png", self)
        self.instantiate_go(enemy)
        self.instantiate_go(player)

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

    def instantiate_go(self, go):
        self.gameobjects.append(go)

    def update(self):
        self.delta_time = self.clock.tick(60) / 1000.0
        for go in self.gameobjects:
            go.update()



    def draw(self):
        self.screen.fill((255, 255, 255))
        for obj in self.gameobjects:
            obj.draw(self.screen)
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
