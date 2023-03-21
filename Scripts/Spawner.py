import os

from overrides import override

from DesignPatterns.ComponentPattern import Component
from Scripts import PrefabCreator, Enums
from Scripts.GameObjectCreator import GameObjectBuilder, GameObjectFactory


class Spawner(Component):

    def __init__(self, world):
        self.world = world
        self.project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
        self.initialize_astroid(Enums.AstroidType.large)
        self.initialize_astroid(Enums.AstroidType.small)

    def serialize(self):
        pass

    @classmethod
    def deserialize(cls, d: dict, owner_go) -> 'Component':
        pass

    @override
    def update(self):
        super().update()

    def initialize_astroid(self, type):

        # Get where the player prefab should be located
        if type == Enums.AstroidType.small:
            astroid_prefab_dir = os.path.join(self.world.prefab_base_dir, "prefab_base_astroid_small.pya")
            astroid_image_path = os.path.join(self.world.project_dir, "Content", "Astroid", "astroid_small.png")
        else:
            astroid_prefab_dir = os.path.join(self.world.prefab_base_dir, "prefab_base_astroid_large.pya")
            astroid_image_path = os.path.join(self.world.project_dir, "Content", "Astroid", "astroid_large.png")

        # Checks if there is a save file on player. If there is use that instead!
        # if not os.path.exists(astroid_prefab_dir):
        #     print("No file found: Creating new small astroid!")
        # 
        #     go_astroid = GameObjectFactory.build_base(x=300, y=400, image_path=astroid_image_path, world=self.world)
        # 
        #     if type == Enums.AstroidType.small:
        #         GameObjectBuilder.add_rigidbody(go=go_astroid,
        #                                         acceleration=(350, 150),
        #                                         friction=(200, 200),
        #                                         max_speed=(350, 250)
        #                                         )
        # 
        #         GameObjectBuilder.add_astroid_small(go=go_astroid)
        #         name = "astroid_small"
        #     else:
        #         GameObjectBuilder.add_rigidbody(go=go_astroid,
        #                                         acceleration=(50, 50),
        #                                         friction=(200, 200),
        #                                         max_speed=(50, 50)
        #                                         )
        # 
        #         GameObjectBuilder.add_astroid_small(go=go_astroid)
        #         name = "astroid_large"
        # 
        #     PrefabCreator.create_prefab_instance(go=go_astroid, go_name=name, prefab_file_path=astroid_prefab_dir)
        # else:
        #     print("File found: Creating player from file!")
        #     go_astroid = PrefabCreator.load_prefab_instance(file_path=astroid_prefab_dir, world=self.world)

        from Scripts.GameObject import Layers
        go_astroid = GameObjectFactory.build_base(x=300, y=400, image_path=astroid_image_path, world=self.world, layer=Layers.FOREGROUND, tag="Asteroid")

        if type == Enums.AstroidType.small:
            GameObjectBuilder.add_rigidbody(go=go_astroid,
                                            acceleration=(350, 150),
                                            friction=(200, 200),
                                            max_speed=(350, 250)
                                            )

            GameObjectBuilder.add_astroid_small(go=go_astroid)
            name = "astroid_small"
        else:
            GameObjectBuilder.add_rigidbody(go=go_astroid,
                                            acceleration=(50, 50),
                                            friction=(200, 200),
                                            max_speed=(50, 50)
                                            )

            GameObjectBuilder.add_astroid_small(go=go_astroid)
            name = "astroid_large"
            
        GameObjectBuilder.add_collision_handler(go_astroid)
            

        self.world.instantiate_go(go=go_astroid)
