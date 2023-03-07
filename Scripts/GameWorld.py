import pygame
import os
import PrefabCreator
from DesignPatterns.StatePattern import StateMachine
from GameObjectCreator import GameObjectFactory, GameObjectBuilder
from GameStates.SubGameStates import PlayGameState, MenuGameState
from Scripts.Spawner import Spawner


class GameWorld:
    def __init__(self, width, height, caption):

        self.menu_game_state = None
        self.play_game_state = None
        self.stateMachine = None
        self.width = width
        self.height = height
        self.caption = caption
        self.gameobjects = []
        self.clock = pygame.time.Clock()
        self.delta_time = None
        self.project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
        self.prefab_base_dir = os.path.join(self.project_dir, "Content", "Prefabs", "Base")
        self.InitializeStates()
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

    def initialize_player(self):

        # Get where the player prefab should be located
        player_prefab_dir = os.path.join(self.prefab_base_dir, "prefab_base_player.pya")

        # Checks if there is a save file on player. If there is use that instead!
        if not os.path.exists(player_prefab_dir):
            print("No file found: Creating new player!")
            player_image_path = os.path.join(self.project_dir, "Content", "Player", "player.png")
            go_player = GameObjectFactory.build_base(x=300, y=400, image_path=player_image_path, world=self)

            GameObjectBuilder.add_rigidbody(go=go_player,
                                            acceleration=(350, 150),
                                            friction=(200, 200),
                                            max_speed=(350, 250)
                                            )

            GameObjectBuilder.add_player(go=go_player)
            boost_image_path = os.path.join(self.project_dir, "Content", "Player", "Boost.png")
            GameObjectBuilder.add_animator(go=go_player, sprite_sheet=boost_image_path, num_frames=5, frame_duration=.1)

            PrefabCreator.create_prefab_instance(go=go_player, go_name="player", prefab_file_path=player_prefab_dir)
        else:
            print("File found: Creating player from file!")
            go_player = PrefabCreator.load_prefab_instance(file_path=player_prefab_dir, world=self)

        self.instantiate_go(go=go_player)

    def initialize_spawner(self):
        spawner = Spawner
        spawner.__init__(self)



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

    def InitializeStates(self):
        self.stateMachine = StateMachine()
        self.play_game_state = PlayGameState(self, self.stateMachine)
        self.menu_game_state = MenuGameState(self, self.stateMachine)
        self.stateMachine.start_statemachine(self.play_game_state)
