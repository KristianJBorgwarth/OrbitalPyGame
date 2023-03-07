from Scripts.AstroidComponent import Astroid
from Scripts.CoreComponents import Transform
from Scripts.GameObject import GameObject
from Enums import AstroidType
from Scripts.PhysicsComponents import Rigidbody
from Scripts.PlayerComponents import Player

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

    # TODO: Add more here

    @staticmethod
    def add_astroid_small(go: GameObject) -> Astroid:
        astroid = Astroid(owner_go=go)
        go.add_component(astroid)
        return astroid

    @staticmethod
    def add_astroid_large(go: GameObject) -> Astroid:
        astroid = Astroid(owner_go=go)
        go.add_component(astroid)
        return astroid


# TODO: Add more here
