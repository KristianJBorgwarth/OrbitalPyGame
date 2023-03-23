import pygame
import os
from Scripts.Core import PrefabCreator
from Scripts.FontManager.fontmanager import FontManager
from Scripts.Core.GameObject import Layers, GameObject
from Scripts.SoundManager.soundmanager import SoundManager
from Scripts.LevelManager.levelmanager import LevelManager
import globals
from Scripts.DesignPatterns.StatePattern import StateMachine
from Scripts.Core.GameObjectCreator import GameObjectFactory, GameObjectBuilder
from Scripts.GameStates.SubGameStates import PlayGameState, MenuGameState, HighScoreMenuState, GameOverState, \
    ControlMenuState
from Scripts.Enviroment.Actor.Spawner import Spawner
from Scripts.Components.animation import Animation


class GameWorld:
    def __init__(self):
        self.render_layers = [[] for _ in range(len(Layers))]
        globals.soundManager = SoundManager()
        globals.soundManager.play_music("menu")
        globals.levelManager = LevelManager()
        self.menu_game_state = None
        self.play_game_state = None
        self.game_over_game_state = None
        self.highscore_game_state = None
        self.controls_game_state = None
        self.list_of_events = None
        self.stateMachine = None
        globals.screen_width = 1920
        globals.screen_height = 1080
        self.caption = "Orbital 2.0"
        self.gameobjects = []
        self.colliding_gameobjects = []
        self.gameobjects_to_destroy = []
        self.clock = pygame.time.Clock()
        self.delta_time = None
        self.project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
        globals.project_path = self.project_dir
        self.prefab_base_dir = os.path.join(self.project_dir, "Content", "Prefabs", "Base")
        pygame.init()
        globals.fontManager = FontManager(
            os.path.join(self.project_dir, "Scripts", "FontManager", "Fonts", "Arcade.TTF"))
        self.screen = pygame.display.set_mode((globals.screen_width, globals.screen_height))
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption(self.caption)
        self.InitializeStates()

    def initialize_player(self):

        # Get where the player prefab should be located
        player_prefab_dir = os.path.join(self.prefab_base_dir, "prefab_base_player.pya")

        # Checks if there is a save file on player. If there is use that instead!
        # if not os.path.exists(player_prefab_dir):
        #     print("No file found: Creating new player!")
        #     player_image_path = os.path.join(self.project_dir, "Content", "Player", "player.png")
        #     go_player = GameObjectFactory.build_base(x=300, y=400, image_path=player_image_path, world=self)
        # 
        #     GameObjectBuilder.add_rigidbody(go=go_player,
        #                                     acceleration=(350, 150),
        #                                     friction=(200, 200),
        #                                     max_speed=(350, 250)
        #                                     )
        # 
        #     GameObjectBuilder.add_player(go=go_player)
        #     idle_image_path = os.path.join(self.project_dir, "Content", "Player", "Idle.png")
        #     boost_image_path = os.path.join(self.project_dir, "Content", "Player", "Boost.png")
        #     animations_list = [Animation("idle", idle_image_path, 1, 1, ),
        #                        Animation("boost", boost_image_path, 5, .1, )]
        #     GameObjectBuilder.add_animator(animations_list, go=go_player)
        # 
        #     PrefabCreator.create_prefab_instance(go=go_player, go_name="player", prefab_file_path=player_prefab_dir)
        # else:
        #     print("File found: Creating player from file!")
        #     go_player = PrefabCreator.load_prefab_instance(file_path=player_prefab_dir, world=self)

        print(os.path.join(self.project_dir, "Scripts", "FontManager", "Fonts", "Arcade.TTF"))
        player_image_path = os.path.join(self.project_dir, "Content", "Player", "player.png")
        go_player = GameObjectFactory.build_base(x=600, y=600, image_path=player_image_path, world=self,
                                                 layer=Layers.FOREGROUND, tag="Player")

        GameObjectBuilder.add_rigidbody(go=go_player,
                                        acceleration=(350, 150),
                                        friction=(200, 200),
                                        max_speed=(350, 250)
                                        )

        GameObjectBuilder.add_collision_handler(go=go_player)
        GameObjectBuilder.add_player(go=go_player)
        idle_image_path = os.path.join(self.project_dir, "Content", "Player", "Idle.png")
        boost_image_path = os.path.join(self.project_dir, "Content", "Player", "Boost.png")
        animations_list = [Animation("idle", idle_image_path, 1, 1, ),
                           Animation("boost", boost_image_path, 5, .1, )]
        GameObjectBuilder.add_animator(animations_list, go=go_player)
        self.instantiate_go(go=go_player)

    def initialize_spawner(self):
        spawner = Spawner
        spawner.__init__(self)

    def instantiate_go(self, go):
        self.gameobjects.append(go)

        if isinstance(go, GameObject):
            self.render_layers[go.layer.value].append(go)

    def destroy_go(self, go):
        self.gameobjects_to_destroy.append(go)

    def destroy_all_go(self):
        for obj in self.gameobjects:
            self.gameobjects_to_destroy.append(obj)

    def clear_removed_objects(self):
        for go in self.gameobjects_to_destroy:
            if isinstance(go, GameObject):
                if go in self.gameobjects:
                    self.gameobjects.remove(go)
                if go in self.render_layers[go.layer.value]:
                    self.render_layers[go.layer.value].remove(go)
            else:
                if go in self.gameobjects:
                    self.gameobjects.remove(go)

            self.gameobjects_to_destroy.remove(go)

    def update(self):
        self.delta_time = self.clock.tick(60) / 1000.0
        self.stateMachine.currentState.execute()
        self.stateMachine.currentState.state_transition()

    def draw(self):
        self.stateMachine.currentState.draw(self.screen)

        pygame.display.flip()

    def start(self):
        running = True
        while running:
            self.list_of_events = pygame.event.get()
            for event in self.list_of_events:
                if event.type == pygame.QUIT:
                    running = False
            self.update()
            self.draw()
        pygame.quit()

    def InitializeStates(self):
        self.stateMachine = StateMachine()
        self.play_game_state = PlayGameState(self, self.stateMachine)
        self.menu_game_state = MenuGameState(self, self.stateMachine)
        self.game_over_game_state = GameOverState(self, self.stateMachine)
        self.highscore_game_state = HighScoreMenuState(self, self.stateMachine)
        self.controls_game_state = ControlMenuState(self, self.stateMachine)
        self.stateMachine.start_statemachine(self.menu_game_state)
