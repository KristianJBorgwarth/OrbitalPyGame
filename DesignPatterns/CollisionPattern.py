import pygame

from DesignPatterns.ComponentPattern import Component


class CollisionHandler(Component):

    def __init__(self, owner_go):
        super().__init__(owner_go)
        self.collision_rules = []

    def on_collision_enter(self, other_go):
        if self.collision_rules.__contains__(other_go.tag):
            return

        self.owner.collision_color = pygame.Color(0, 255, 0)

    def on_collision(self, other_go):
        if self.collision_rules.__contains__(other_go.tag):
            return

    def on_collision_exit(self, other_go):
        if self.collision_rules.__contains__(other_go.tag):
            return

        self.owner.collision_color = pygame.Color(255, 0, 0)

    def add_collision_rule(self, tag):
        if self.collision_rules.__contains__(tag):
            return
        else:
            self.collision_rules.append(tag)

    def update(self):
        super().update()

    def serialize(self):
        pass

    @classmethod
    def deserialize(cls, d: dict, owner_go) -> 'Component':
        pass


class PlayerCollisionHandler(CollisionHandler):
    def on_collision_enter(self, other_go):
        super().on_collision_enter(other_go)
        print("THIS IS THE PLAYER")

    def on_collision(self, other_go):
        super().on_collision(other_go)

    def on_collision_exit(self, other_go):
        super().on_collision_exit(other_go)


class AsteroidCollisionHandler(CollisionHandler):
    def on_collision_enter(self, other_go):
        super().on_collision_enter(other_go)
        print("THIS IS THE ASTEROID")

    def on_collision(self, other_go):
        super().on_collision(other_go)

    def on_collision_exit(self, other_go):
        super().on_collision_exit(other_go)
        

# Define the collision handler map as a global variable
collision_handler_map = {
    "Player": PlayerCollisionHandler,
    "Asteroid": AsteroidCollisionHandler,
    # Add more game objects and collision handler classes as needed
}
