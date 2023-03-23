import os

import pygame.mixer


class SoundManager:
    def __init__(self):
        self.sound_effect_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
        self.sound_dir = os.path.join(self.sound_effect_dir, "Sounds", "Sound")
        self.music_dir = os.path.join(self.sound_effect_dir, "Sounds", "Music")
        pygame.mixer.init()
        self.sound_volume = 0.3
        self.music_volume = 0.1
        self.sounds = {
            #'move': pygame.mixer.Sound('Sounds/Sound/'),
            'shoot': pygame.mixer.Sound(os.path.join(self.sound_dir, "laser.ogg")),
            'take_damage': pygame.mixer.Sound(os.path.join(self.sound_dir, "hit.ogg")),
            'player_death': pygame.mixer.Sound(os.path.join(self.sound_dir, "death.ogg")),
            'enemy_death': pygame.mixer.Sound(os.path.join(self.sound_dir, "explosion.ogg")),
        }
        self.music = {
            'menu': pygame.mixer.Sound(os.path.join(self.music_dir, "bg_music.ogg")),
        }

    def play_sound(self, sound):
        self.sounds[sound].set_volume(self.sound_volume)
        self.sounds[sound].play()

    def play_music(self, music):
        self.music[music].set_volume(self.music_volume)
        self.music[music].play()
