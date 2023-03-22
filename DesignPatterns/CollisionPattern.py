import pygame

from DesignPatterns.ComponentPattern import Component


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
        if other_go.tag == "Player_Projectile":
            self.owner.world.destroy_go(self.owner)

    def on_collision_exit(self, other_go):
        if super().on_collision_exit(other_go):
            return


class Split_Asteroid_CollisionHandler(CollisionHandler):
    def on_collision_enter(self, other_go):
        if super().on_collision_enter(other_go):
            return
        if other_go.tag == "Player_Projectile":
            self.owner.world.destroy_go(self.owner)

    def on_collision_exit(self, other_go):
        if super().on_collision_exit(other_go):
            return


class Large_Asteroid_CollisionHandler(CollisionHandler):
    def on_collision_enter(self, other_go):
        if super().on_collision_enter(other_go):
            return
        print(self.owner.tag)
        print(other_go.tag)
        if other_go.tag == "Player_Projectile":
            from Enviroment.Actor.ActorFactory import AstroidFactory, AstroidType
            for i in range(4):
                self.owner.world.instantiate_go(AstroidFactory().CreateProduct(AstroidType.SplitAstroid, self.owner.world,
                                                                            (self.owner.transform.position.x,
                                                                             self.owner.transform.position.y)))


            self.owner.world.destroy_go(self.owner)
        if other_go.tag == "Asteroid_Large":
            self.owner.world.destroy_go(self.owner)

    def on_collision_exit(self, other_go):
        if super().on_collision_exit(other_go):
            return


# Define the collision handler map as a global variable
collision_handler_map = {
    "Player": Player_CollisionHandler,
    "Asteroid_Small": Small_Asteroid_CollisionHandler,
    "Asteroid_Large": Large_Asteroid_CollisionHandler,
    "Asteroid_Split": Split_Asteroid_CollisionHandler,
    "Player_Projectile": Player_Projectile_CollisionHandler,
    # Add more game objects and collision handler classes as needed
}
