import pygame

import globals
from Scripts.DesignPatterns.ComponentPattern import Component


class CollisionHandler(Component):

    def __init__(self, owner_go):
        super().__init__(owner_go)
        self.collision_rules = []

    def on_collision_enter(self, other_go):
        if other_go.tag in self.collision_rules:
            return True
        self.owner.collision_color = pygame.Color(0, 255, 0)
        return False

    def on_collision(self, other_go):
        if other_go.tag in self.collision_rules:
            return True

        return False

    def on_collision_exit(self, other_go):
        if other_go.tag in self.collision_rules:
            return True

        self.owner.collision_color = pygame.Color(255, 0, 0)
        return False

    def add_collision_rule(self, tag):
        if tag in self.collision_rules:
            return
        self.collision_rules.append(tag)


class Player_CollisionHandler(CollisionHandler):
    def on_collision_enter(self, other_go):
        if super().on_collision_enter(other_go):
            return


    def on_collision_exit(self, other_go):
        if super().on_collision_exit(other_go):
            return


class Player_Projectile_CollisionHandler(CollisionHandler):
    def on_collision_enter(self, other_go):
        if super().on_collision_enter(other_go):
            return
        self.owner.world.destroy_go(self.owner)

    def on_collision_exit(self, other_go):
        if super().on_collision_exit(other_go):
            return


class Small_Asteroid_CollisionHandler(CollisionHandler):
    def on_collision_enter(self, other_go):
        if super().on_collision_enter(other_go):
            return
        # player projectile colliding with small asteroid
        # 3 points
        if other_go.tag == "Player_Projectile":
            globals.soundManager.play_sound("hit")
            globals.score += 3
            self.owner.world.destroy_go(self.owner)
        if other_go.tag == "Player":
            globals.soundManager.play_sound("explosion")
            globals.player_health -= 7
            self.owner.world.destroy_go(self.owner)

    def on_collision_exit(self, other_go):
        if super().on_collision_exit(other_go):
            return


class Split_Asteroid_CollisionHandler(CollisionHandler):
    def on_collision_enter(self, other_go):
        if super().on_collision_enter(other_go):
            return
        # player projectile colliding with split/small asteroid
        # 3 points
        if other_go.tag == "Player_Projectile":
            globals.soundManager.play_sound("hit")
            globals.score += 3
            self.owner.world.destroy_go(self.owner)
        if other_go.tag == "Player":
            globals.soundManager.play_sound("explosion")
            globals.player_health -= 7
            self.owner.world.destroy_go(self.owner)


    def on_collision_exit(self, other_go):
        if super().on_collision_exit(other_go):
            return


class Large_Asteroid_CollisionHandler(CollisionHandler):
    def on_collision_enter(self, other_go):
        if super().on_collision_enter(other_go):
            return
        # player projectile colliding with large asteroid
        # 10 points
        if other_go.tag == "Player_Projectile":
            from Scripts.Enviroment.Actor.ActorFactory import AstroidFactory, AstroidType
            globals.soundManager.play_sound("hit")
            globals.score += 10
            for i in range(3):
                self.owner.world.instantiate_go(AstroidFactory().
                                                CreateProduct(AstroidType.SplitAstroid,
                                                               self.owner.world,
                                                              (self.owner.transform.position.x,
                                                               self.owner.transform.position.y)))
            self.owner.world.destroy_go(self.owner)
        # Large asteroid colliding with large asteroid
        # no points
        if other_go.tag == "Asteroid_Large":
            from Scripts.Enviroment.Actor.ActorFactory import AstroidFactory, AstroidType
            self.owner.world.instantiate_go(AstroidFactory().
                                            CreateProduct(AstroidType.SplitAstroid,
                                                          self.owner.world,
                                                          (self.owner.transform.position.x,
                                                           self.owner.transform.position.y)))
            globals.soundManager.play_sound("hit")
            self.owner.world.destroy_go(self.owner)
        # Player colliding with large astroid
        if other_go.tag == "Player":
            globals.soundManager.play_sound("explosion")
            globals.player_health -= 40
            self.owner.world.destroy_go(self.owner)

    def on_collision_exit(self, other_go):
        if super().on_collision_exit(other_go):
            return

class Enemy_CollisionHandler(CollisionHandler):

    def on_collision_enter(self, other_go):
        if super().on_collision_enter(other_go):
            return

    def on_collision_exit(self, other_go):
        if super().on_collision_exit(other_go):
            return
        
class Enemy_Projectile_CollisionHandler(CollisionHandler):

    def on_collision_enter(self, other_go):
        if super().on_collision_enter(other_go):
            return

    def on_collision_exit(self, other_go):
        if super().on_collision_exit(other_go):
            return


# Define the collision handler map as a global variable
collision_handler_map = {
    "Player": Player_CollisionHandler,
    "Enemy_Base": Enemy_CollisionHandler,
    "Enemy_Boss": Enemy_CollisionHandler,
    "Asteroid_Small": Small_Asteroid_CollisionHandler,
    "Asteroid_Large": Large_Asteroid_CollisionHandler,
    "Asteroid_Split": Split_Asteroid_CollisionHandler,
    "Player_Projectile": Player_Projectile_CollisionHandler,
    "Enemy_Projectile": Enemy_Projectile_CollisionHandler,
    # Add more game objects and collision handler classes as needed
}
