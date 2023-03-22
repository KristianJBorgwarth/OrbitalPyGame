# level_manager.py
import globals


class LevelManager:
    def __init__(self, level_up_score=5000):
        self.level_up_score = level_up_score

    def update_level(self):
        if globals.score >= self.level_up_score * globals.level:
            globals.level += 1

    def reset(self):
        globals.score = 0
        globals.level = 1
