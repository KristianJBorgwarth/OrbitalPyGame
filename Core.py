import json
import os

import pygame
from GameObject import GameObject
from Components import Rigidbody, Player, Transform


class GameWorld:
    def __init__(self, width, height, caption):
        self.width = width
        self.height = height
        self.caption = caption
        self.gameobjects = []
        self.clock = pygame.time.Clock()
        self.delta_time = None

        # Checks if there is a save file on player. If there is use that instead!
        # TODO: Comment later
        if not os.path.exists("prefab_base_player.pya"):
            print("No file found: Creating new player!")
            player = GameObject(300, 400, "Content\Player\player.png", self)
            player.add_component(
                Rigidbody(acceleration=(350, 150), friction=(200, 200), max_speed=(350, 250), owner_go=player))
            player.add_component(Player(player))

            data = json.dumps(player.serialize_gameobject("player"), indent=4)

            with open("prefab_base_player.pya", "w") as f:
                f.write(data, )
        else:
            print("File found: Creating player from file!")
            player = self.create_game_object_from_json("prefab_base_player.pya")

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

    def create_game_object_from_json(self, file_path):
        # Open the JSON file specified by file_path
        with open(file_path, 'r') as file:
            # Load the JSON data into a Python dictionary
            data = json.load(file)

        # Create a new GameObject instance using data from the JSON file
        go = GameObject(data["initial_position"]["x"], data["initial_position"]["y"], data['image_path'], self)

        # Loop through the components defined in the JSON file
        for component_data in data['components']:
            # Determine the type of component based on the 'type' field in the JSON data
            component_type = component_data['type']

            # Create a new component based on the data in the JSON file and add it to the GameObject
            if component_type == 'Transform':
                transform = Transform.deserialize(component_data)
                transform.position = pygame.math.Vector2(data['initial_position']['x'], data['initial_position']['y'])
                go.add_component(transform)
            elif component_type == 'Rigidbody':
                rigidbody = Rigidbody.deserialize(component_data)
                go.add_component(rigidbody)
            elif component_type == 'Player':
                player = Player(go)
                go.add_component(player)
            else:
                # If the component type is not recognized, raise an error
                raise ValueError(f'Invalid component type: {component_type}')

        data = json.dumps(go.serialize_gameobject("player"), indent=4)

        # Load the JSON file into a dictionary
        with open('prefab_base_player.pya', 'r') as f:
            data = json.load(f)

        # Modify the position of the Transform Component's position
        # This is in case we change the initial_position
        data['components'][0]['position'] = [go.initial_position.x, go.initial_position.y]

        # Write the updated data back to the JSON file
        with open('prefab_base_player.pya', 'w') as f:
            json.dump(data, f, indent=4)

        # Return the completed GameObject instance
        return go
