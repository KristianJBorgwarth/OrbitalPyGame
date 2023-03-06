from Scripts.Components import Rigidbody, Transform, Player, Astroid
from Scripts.GameObject import GameObject
from Enums import AstroidType

class GameObjectFactory:
    @staticmethod
    def build_base(x, y, image_path, world) -> GameObject:
        go = GameObject(x, y, image_path, world)
        return go

class GameObjectBuilder:
    @staticmethod
    def add_rigidbody(go: GameObject, acceleration, friction, max_speed) -> Rigidbody:
        rigidbody = Rigidbody(acceleration, friction, max_speed, go)
        go.add_component(rigidbody)
        return rigidbody

    @staticmethod
    def add_player(go: GameObject) -> Player:
        player = Player(go)
        go.add_component(player)
        return player

    @staticmethod
    def add_astroid(go: GameObject) -> Astroid:
        astroid = Astroid(owner_go=go, atype=AstroidType.large)
        go.add_component(astroid)
        return astroid


# TODO: Add more here
