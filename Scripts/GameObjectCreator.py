from Scripts.CoreComponents import Animator
from Scripts.GameObject import GameObject
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

    @staticmethod
    def add_animator(go: GameObject, sprite_sheet, num_frames, frame_duration) -> Animator:
        animator = Animator(sprite_sheet, num_frames, frame_duration, go)
        go.add_component(animator)
        return animator

    # TODO: Add more here
