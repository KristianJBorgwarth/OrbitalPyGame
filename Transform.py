# import pygame.math
# 
# 
# class Transform:
#     def __init__(self, position=(0, 0), rotation=0, scale=(1, 1)):
#         self._position = pygame.math.Vector2(position)
#         self._rotation = rotation
#         self._scale = pygame.math.Vector2(scale)
# 
#     @property
#     def position(self):
#         return self._position
# 
#     @property
#     def rotation(self):
#         return self._rotation
# 
#     @property
#     def scale(self):
#         return self._scale
# 
#     def translate(self, x, y):
#         self._position += pygame.math.Vector2(x, y)
# 
#     def rotate(self, angleAmount):
#         self._rotation = (self._rotation + angleAmount) % 360
# 
#     def scale_by(self, vectorAmount):
#         self._scale *= pygame.math.Vector2(vectorAmount)
