from enum import Enum

class Layers(Enum):
    BACKGROUND = 0
    MIDDLEGROUND = 1
    FOREGROUND = 2

class AstroidType(Enum):
    SMALL = 1
    LARGE = 2
    
class EnemyType(Enum):
    DEFAULT = 1
    BOSS = 2
    
    