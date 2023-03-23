import os
import pygame
from overrides import override

import globals
from DesignPatterns.ComponentPattern import Component
from Scripts.CoreComponents import Animator
from Scripts.GameObject import GameObject, Layers
from Scripts.GameObjectCreator import GameObjectFactory, GameObjectBuilder
from Scripts.PhysicsComponents import Rigidbody

class Player(Component):
    def __init__(self, owner_go: GameObject):
        super().__init__(owner_go)

        self.owner = owner_go
        self.rigidbody = self.owner.get_component(Rigidbody)
        self.projectile_dir = os.path.join(self.owner.world.project_dir, "Content", "Weaponry", "laser.png")

        self.directions = \
            {
                'x': {'positive': pygame.K_h, 'negative': pygame.K_k},
                'y': {'positive': pygame.K_UP, 'negative': pygame.K_DOWN},
            }

        self.forward_dir = pygame.math.Vector2(0, 0)
    
        
        
    def serialize(self):
        d = super().serialize()
        d.update({
            'type': self.__class__.__name__,
        })
        return d

    @classmethod
    @override
    def deserialize(cls, d: dict, owner_go) -> 'Player':
        pass

    @override
    def update(self):
        super().update()

        # Get the forward direction vector based on the player's current rotation
        self.forward_dir = pygame.math.Vector2(1, 0).rotate(-self.owner.transform.rotation)
        # Note the negative sign before go.transform.rotation this is because pygame uses a different coordinate system.

        keys = pygame.key.get_pressed()
        # keys_down stores the value of pygames events
        keys_down = pygame.event.get()
        # Quit on escape
        # loops through the keys_down events
        for k in keys_down:
            # checks the type of event this is for keys that are held down
            if k.type == pygame.KEYDOWN:
                # check if the key held down is space
                if k.key == pygame.K_SPACE:
                    # sets key repeating delay , interval before being able to run this again
                    pygame.key.set_repeat(1, 200)
                    self.ShootProjectile()

        anim = self.owner.get_component(Animator).current_anim
        if anim is not None:
            if keys[pygame.K_RIGHT]:
                self.owner.transform.rotate_image(anim, -5)
            if keys[pygame.K_LEFT]:
                self.owner.transform.rotate_image(anim, 5)

        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            return

        if self.rigidbody is None:
            return

        # self.rigidbody.update_velocity('x', keys, self.directions, self.owner)
        self.rigidbody.update_velocity('y', keys, self.directions, self.owner, self.forward_dir)

    def ShootProjectile(self):
        globals.soundManager.play_sound("shoot")

        offset = pygame.math.Vector2(25, 0)
        projectile_ejection = self.owner.transform.position + offset
        go_projectile = GameObjectFactory.build_base(x=projectile_ejection.x, y=projectile_ejection.y,
                                                     image_path=self.projectile_dir, world=self.owner.world, layer=Layers.MIDDLEGROUND, tag="Player_Projectile")

        GameObjectBuilder.add_collision_handler(go_projectile)
        go_projectile.add_collision_rule("Player")
        go_projectile.add_collision_rule("Player_Projectile")


        GameObjectBuilder.add_rigidbody(go=go_projectile,
                                            acceleration=(6500, 6500),
                                            friction=(0, 0),
                                            max_speed=(1000, 1000)
                                            )
    
        projectile = GameObjectBuilder.add_base_projectile(go=go_projectile, damage=10, direction=self.forward_dir, rotation=self.owner.transform.rotation)
        self.owner.world.instantiate_go(go_projectile)

        projectile.move(self.forward_dir)
