import pygame
import os
import PrefabCreator
from GameObject import GameObject
from Components import Rigidbody, Player  # TODO Remove this after refactoring to factory & builder
from  GameObjectCreator import GameObjectFactory, GameObjectBuilder


class GameWorld:
    def __init__(self, width, height, caption):
        
        self.width = width
        self.height = height
        self.caption = caption
        self.gameobjects = []
        self.clock = pygame.time.Clock()
        self.delta_time = None
        self.project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
        self.prefab_base_dir = os.path.join(self.project_dir, "Content", "Prefabs", "Base")

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

        self._initialize_player()

    
    def _initialize_player(self):
        
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

            PrefabCreator.create_prefab_instance(go=go_player, go_name="player", prefab_file_path=player_prefab_dir)
        else:
            print("File found: Creating player from file!")
            go_player = PrefabCreator.load_prefab_instance(file_path=player_prefab_dir, world=self)

        self.instantiate_go(go=go_player)

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
        