import random

import globals


class Behaviour:
    def __init__(self, enemy):
        self.enemy = enemy
        self.transform = self.enemy.owner.transform
        self.image = self.enemy.owner.image

    def update(self):
        pass


class BasePatrolBehaviour(Behaviour):
    def __init__(self, enemy):
        from Scripts.Components.PhysicsComponents import Rigidbody
        super().__init__(enemy)
        self.direction = 1
        self.set_initial_position()
        self.rb = self.enemy.owner.get_component(Rigidbody)

        print(self.direction)

    def update(self):
        super().update()
        self.patrol()

    def set_initial_position(self):
        if self.direction == -1:
            self.transform.position.x = globals.screen_width - self.image.get_width()
        else:
            self.transform.position.x = 0

        self.transform.position.y = 0 + self.image.get_height()

    def patrol(self):



class BaseAttackBehaviour(Behaviour):
    def __init__(self, enemy):
        super().__init__(enemy)

    def update(self):
        super().update()


# Define the behaviour map as a global variable
behaviour_mapping = {
    "Base_Patrol": BasePatrolBehaviour,
    "Base_Attack": BaseAttackBehaviour,
    # "Boss_Patrol": BossPatrolBehaviour,
    # "Boss_Attack": BossAttackBehaviour,
    # Add more game objects and collision handler classes as needed
}
