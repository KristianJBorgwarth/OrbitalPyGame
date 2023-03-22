from DesignPatterns.CollisionPattern import CollisionHandler, collision_handler_map
from Enviroment.Actor.AstroidComponent import Astroid
from Scripts.CoreComponents import Animator
from Scripts.GameObject import GameObject
from Scripts.PhysicsComponents import Rigidbody
from Scripts.Projectile import BaseProjectile


class GameObjectFactory:
    @staticmethod
    def build_base(x, y, image_path, world, layer, tag="null") -> GameObject:
        go = GameObject(x, y, image_path, world, layer=layer, tag=tag)
        return go


class GameObjectBuilder:
    @staticmethod
    def add_rigidbody(go: GameObject, acceleration, friction, max_speed) -> Rigidbody:
        rigidbody = Rigidbody(acceleration, friction, max_speed, go)
        go.add_component(rigidbody)
        return rigidbody

    @staticmethod
    def add_player(go: GameObject):
        from Scripts.PlayerComponents import Player
        player = Player(go)
        go.add_component(player)
        go.add_collision_rule("Player_Projectile")
        return player

    @staticmethod
    def add_animator(animations_list, go: GameObject) -> Animator:
        animator = Animator(go, animations_list)
        go.add_component(animator)
        return animator

    
    @staticmethod
    def add_base_projectile(go: GameObject, damage, direction, rotation) -> BaseProjectile:
        projectile = BaseProjectile(owner_go=go, damage=damage, forward_dir=direction, rotation=rotation)
        go.add_component(projectile)    
        return projectile
    
    @staticmethod
    def add_collision_handler(go: GameObject) -> CollisionHandler:
        collision_handler = collision_handler_map.get(go.tag, CollisionHandler)
        collision = collision_handler(go)
        go.add_component(collision)
        return collision

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
