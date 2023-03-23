import os
import random

import pygame

import globals
from Scripts.Extensions.ExtensionsEnum import Layers


class Behaviour:
    def __init__(self, enemy):
        self.enemy = enemy
        self.transform = self.enemy.owner.transform
        self.image = self.enemy.owner.image

    def update(self):
        pass


class DefaultPatrolBehaviour(Behaviour):
    def __init__(self, enemy):
        from Scripts.Components.PhysicsComponents import Rigidbody
        super().__init__(enemy)
        self.direction = -1
        self.set_initial_position()
        self.rb = self.enemy.owner.get_component(Rigidbody)
        self.target_x = globals.screen_width if self.direction == 1 else 0
        self.distance_threshold = 50  # This can be adjusted based on how close you want the object to be before slowing down

    def update(self):
        super().update()
        self.patrol()

    def set_initial_position(self):
        if self.direction == -1:
            self.transform.position.x = globals.screen_width - self.image.get_width()
        else:
            self.transform.position.x = 0

        self.transform.position.y = 0 + self.image.get_height()
        self.transform.rotate_image(self.image, -45)

    def patrol(self):
        if self.direction == -1:
            if self.transform.position.x <= self.image.get_width():
                self.rb.velocity = (0,0)
                self.direction = 1
        else:
            if self.transform.position.x >= globals.screen_width - self.image.get_width():
                self.rb.velocity = (0,0)
            
                self.direction = -1

        self.rb.add_force((self.direction, 0), self.enemy.owner)


class DefaultAttackBehaviour(Behaviour):
    def __init__(self, enemy):
        super().__init__(enemy)
        self.last_shot_time = 0
        self.cooldown_time = 1000  # set the cooldown time in milliseconds

    def update(self):
        super().update()
        self.ShootProjectile()

    def ShootProjectile(self):
        from Scripts.Core.GameObjectCreator import GameObjectBuilder
        from Scripts.Core.GameObjectCreator import GameObjectFactory

        current_time = pygame.time.get_ticks()
        time_since_last_shot = current_time - self.last_shot_time
        if time_since_last_shot < self.cooldown_time:
            return
    
        # If enough time has passed, update last shot time
        self.last_shot_time = current_time

        globals.soundManager.play_sound("shoot")

        img_path = os.path.join(globals.project_path, "Content", "Weaponry", "laser.png")

        offset = pygame.math.Vector2(0, 75)
        projectile_ejection = self.enemy.owner.transform.position + offset
        go_projectile = GameObjectFactory.build_base(x=projectile_ejection.x, y=projectile_ejection.y,
                                                     image_path=img_path, world=self.enemy.owner.world, layer=Layers.MIDDLEGROUND, tag="Enemy_Projectile")

        GameObjectBuilder.add_collision_handler(go_projectile)
        go_projectile.add_collision_rule("Enemy_Base")
        go_projectile.add_collision_rule("Enemy_Projectile")


        rb = GameObjectBuilder.add_rigidbody(go=go_projectile,
                                        acceleration=(750, 750),
                                        friction=(0, 0),
                                        max_speed=(1000, 1000)
                                        )

        GameObjectBuilder.add_base_projectile(go=go_projectile, damage=10, direction=(0, 1), rotation=90)
        rb.velocity = (0, 1000)
        self.enemy.owner.world.instantiate_go(go_projectile)
        
        
class BossAttackBehaviour(Behaviour):
    def __init__(self, enemy):
        super().__init__(enemy)
        self.last_shot_time = 0
        self.cooldown_time = 250  # set the cooldown time in milliseconds
    
    def update(self):
        super().update()
        self.ShootProjectile()

    def ShootProjectile(self):
        from Scripts.Core.GameObjectCreator import GameObjectBuilder
        from Scripts.Core.GameObjectCreator import GameObjectFactory
    
        current_time = pygame.time.get_ticks()
        time_since_last_shot = current_time - self.last_shot_time
        if time_since_last_shot < self.cooldown_time:
            return
    
        # If enough time has passed, update last shot time
        self.last_shot_time = current_time
    
        globals.soundManager.play_sound("shoot")
    
        img_path = os.path.join(globals.project_path, "Content", "Weaponry", "laser.png")
    
        offset = pygame.math.Vector2(0, 75)
        projectile_ejection = self.enemy.owner.transform.position + offset
        go_projectile = GameObjectFactory.build_base(x=projectile_ejection.x, y=projectile_ejection.y,
                                                     image_path=img_path, world=self.enemy.owner.world, layer=Layers.MIDDLEGROUND, tag="Enemy_Projectile")
    
        GameObjectBuilder.add_collision_handler(go_projectile)
        go_projectile.add_collision_rule("Enemy_Base")
        go_projectile.add_collision_rule("Enemy_Projectile")
    
        rb = GameObjectBuilder.add_rigidbody(go=go_projectile,
                                             acceleration=(750, 750),
                                             friction=(0, 0),
                                             max_speed=(1000, 1000)
                                             )
    
        GameObjectBuilder.add_base_projectile(go=go_projectile, damage=25, direction=(0, 1), rotation=90)
        rb.velocity = (0, 1000)
        self.enemy.owner.world.instantiate_go(go_projectile)
    


# Define the behaviour map as a global variable
behaviour_mapping = {
    "Base_Patrol": DefaultPatrolBehaviour,
    "Base_Attack": DefaultAttackBehaviour,
    "Boss_Attack": BossAttackBehaviour,
    # Add more game objects and collision handler classes as needed
}
