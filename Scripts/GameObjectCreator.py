from Scripts.CoreComponents import Animator
from Scripts.GameObject import GameObject
from Scripts.PhysicsComponents import Rigidbody
from Scripts.PlayerComponents import Player
from Scripts.animation import Animation


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
    def add_animator(animation_list, go: GameObject) -> Animator:
        animator = Animator(go, animation_list)
        go.add_component(animator)
        return animator



    # TODO: Add more here
