import pygame

soundManager = None
fontManager = None
levelManager = None
highscore_manager = None

width = 1920
height = 1080
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
project_path = None
start_event = None
quit_event = None
highscore_event = None
controls_event = None
player_is_dead = False
play_again_event = None
back_event = None


#Game Object Size
go_size_scale = 0.85

#UI font elements
high_score = 0
score = 0
level = 1
astroidCount = 0
player_health = 100

class Stages(Enum):
    one = 100
    two = 200
    three = 300
    four = 400