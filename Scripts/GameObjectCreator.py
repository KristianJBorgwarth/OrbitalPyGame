from Scripts.Components import Rigidbody, Transform, Player
from Scripts.GameObject import GameObject


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
