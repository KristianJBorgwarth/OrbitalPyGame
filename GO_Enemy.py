from overrides import override

from GameObject import GameObject
from Components import Rigidbody
from AI.AI import Bot


class Enemy(GameObject):
    def __init__(self, x, y, image, world):
        super().__init__(x, y, image, world)
        self.rigidbody = Rigidbody(acceleration=(350, 150), friction=(200, 200), max_speed=(350, 250))
        self.bot = Bot()


    @override
    def update(self):
        super().update()
        self.transform.translate(*self.rigidbody.velocity * self.world.delta_time)
        self.bot.update(self.rigidbody, self.world)




