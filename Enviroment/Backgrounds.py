from overrides import override

from GameObject import GameObject


class MenuBackground(GameObject):
    def __init__(self, x, y, image, world):
        super().__init__(x, y, image, world)

    @override
    def update(self):
        self.scroll_backGround()

    @override()
    def draw(self, screen):
        screen.blit(self.image, self.transform.position)
        screen.blit(self.image, (self.transform.position.x, self.transform.position.y - self.image.get_height()))

    def scroll_backGround(self):
        scroll_speed = 5
        self.transform.position.y += scroll_speed
        if self.transform.position.y > self.image.get_height():
            self.transform.position.y = 0

