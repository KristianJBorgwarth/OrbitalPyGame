# THIS IS A QUICK EXAMPLE. NOT SURE IF IT WORKS!! - Nichlas
# TODO: Implement this shit


# class GameObjectFactory:
#     @staticmethod
#     def create_basic_object(x, y, image_path, world):
#         go = GameObject(x, y, image_path, world)
#         transform = Transform(go)
#         go.add_component(transform)
#         return go

# class GameObjectBuilder:
#     def __init__(self, go):
#         self.go = go

#     def add_rigidbody(self, acceleration, friction, max_speed):
#         rigidbody = Rigidbody(acceleration, friction, max_speed, self.go)
#         self.go.add_component(rigidbody)
#         return self

#     def add_player(self):
#         player = Player(self.go)
#         self.go.add_component(player)
#         return self

# # Example usage:
# go = GameObjectFactory.create_basic_object(300, 400, "Content\Player\player.png", self)
# builder = GameObjectBuilder(go)
# builder.add_rigidbody(acceleration=(350, 150), friction=(200, 200), max_speed=(350, 250))
# builder.add_player()
