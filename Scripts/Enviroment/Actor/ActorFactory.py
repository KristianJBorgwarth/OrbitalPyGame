import os
import random
from typing import Any

import globals
from Scripts.DesignPatterns.BehaviourPattern import DefaultPatrolBehaviour, DefaultAttackBehaviour, behaviour_mapping
from Scripts.DesignPatterns.FactoryPattern import AbstractFactory
from Scripts.Core.GameObjectCreator import GameObjectFactory, GameObjectBuilder
from Scripts.Core.GameObject import GameObject, Layers
from Scripts.Extensions.ExtensionsEnum import AstroidType, EnemyType


class AstroidFactory(AbstractFactory):
    def __init__(self):
        self.x = None
        self.y = None
        self.ranPoint = None

    def CreateProduct(self, enum: AstroidType, game_world) -> GameObject:
        if enum is AstroidType.SMALL:
            img_path = os.path.join(globals.project_path, "Content", "Astroid", "astroid_small.png")
            img_width = 16
            img_height = 16

            self.ranPoint = random.choice(
                [(random.randrange(0, globals.screen_width - img_width),
                  random.choice([-1 * img_height - 5, globals.screen_height + 5])),
                 (random.choice([-1 * img_width - 5, globals.screen_width + 5]),
                  random.randrange(0, globals.screen_height - img_height))])

            self.x, self.y = self.ranPoint

            asteroid_go = GameObjectFactory.build_base(x=self.x, y=self.y, image_path=img_path, world=game_world,
                                                       layer=Layers.FOREGROUND, tag="Asteroid_Small")

            GameObjectBuilder.add_astroid_small(asteroid_go)

        if enum is AstroidType.LARGE:
            img_path = os.path.join(globals.project_path, "Content", "Astroid", "astroid_large.png")
            img_width = 117
            img_height = 109

            self.ranPoint = random.choice(
                [(random.randrange(0, globals.screen_width - img_width),
                  random.choice([-1 * img_height - 5, globals.screen_height + 5])),
                 (random.choice([-1 * img_width - 5, globals.screen_width + 5]),
                  random.randrange(0, globals.screen_height - img_height))])

            self.x, self.y = self.ranPoint

            asteroid_go = GameObjectFactory.build_base(x=self.x, y=self.y, image_path=img_path, world=game_world,
                                                       layer=Layers.FOREGROUND, tag="Asteroid_Large")
            GameObjectBuilder.add_astroid_large(asteroid_go)

        GameObjectBuilder.add_collision_handler(asteroid_go)

        # Add Collision rules here
        # asteroid_go.add_collision_rule("Player")

        return asteroid_go


class EnemyFactory(AbstractFactory):

    def CreateProduct(self, enum: EnemyType, game_world) -> Any:

        if enum is EnemyType.DEFAULT:
            img_path = os.path.join(globals.project_path, "Content", "Enemy", "Enemy_Base.png")
            tag = "Enemy_Base"
            behaviour_tags = ["Base_Attack", "Base_Patrol"]
            
        else:
            img_path = os.path.join(globals.project_path, "Content", "Enemy", "Enemy_Base.png")
            tag = "Enemy_Boss"
            behaviour_tags = ["Boss_Attack", "Base_Patrol"]

        enemy_go = GameObjectFactory.build_base(x=0, y=0, image_path=img_path, world=game_world,
                                                layer=Layers.FOREGROUND, tag=tag)
            
        GameObjectBuilder.add_rigidbody(go=enemy_go,
                                        acceleration=(350, 150),
                                        friction=(200, 200),
                                        max_speed=(350, 250)
                                        )

        enemy_comp = GameObjectBuilder.add_enemy(enemy_go)
        
        for tag in behaviour_tags:
            behaviour_class = behaviour_mapping.get(tag)
            enemy_comp.add_behaviour(behaviour_class(enemy_comp))


        GameObjectBuilder.add_collision_handler(enemy_go)
        enemy_go.add_collision_rule(enemy_go.tag)
        enemy_go.add_collision_rule("Enemy_Projectile")
        return enemy_go
        