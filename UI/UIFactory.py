import os
import pygame
import globals
from DesignPatterns.FactoryPattern import AbstractFactory
from UI.UIComponents import UIButton, ScrollingBackGround, UIDecor
from UI.UIObjects import UIObject
from enum import Enum


class UIButtonProduct(Enum):
    StartButton = 1
    ExitButton = 2
    HighScoreButton = 3
    PlayAgainButton = 4
    BackButton = 5
    ControlsButton = 6


class UIBackground(Enum):
    MenuBackGround = 1
    EasyDiffBackground = 2
    HardDiffBackground = 3
    BossDiffBackground = 4
    GameOverBackground = 5


class UIDecorProduct(Enum):
    GameOverText = 1
    HighScoreText = 2


class ButtonFactory(AbstractFactory):

    def __init__(self):
        globals.start_event = pygame.USEREVENT + 1
        pygame.event.set_allowed(pygame.USEREVENT + 1)
        globals.quit_event = pygame.USEREVENT + 2
        pygame.event.set_allowed(globals.quit_event)
        globals.play_again_event = pygame.USEREVENT + 3
        pygame.event.set_allowed(globals.play_again_event)
        globals.back_event = pygame.USEREVENT + 4
        pygame.event.set_allowed(globals.back_event)
        globals.highscore_event = pygame.USEREVENT + 5
        pygame.event.set_allowed(globals.highscore_event)
        globals.controls_event = pygame.USEREVENT + 6
        pygame.event.set_allowed(globals.controls_event)

    def CreateProduct(self, enum: UIButtonProduct, game_world) -> UIObject:
        gw = game_world
        if enum is UIButtonProduct.StartButton:
            button_go = UIObject(gw, 825, 300)
            start_img_path = os.path.join(globals.project_path, "Content", "GUI", "play.png")
            start_img_path_h = os.path.join(globals.project_path, "Content", "GUI", "play_hover.png")
            button_go.add_component(UIButton(button_go, start_img_path, start_img_path_h, globals.start_event))
            return button_go

        elif enum is UIButtonProduct.ExitButton:
            button_go = UIObject(gw, 845, 600)
            exit_b_img_path = os.path.join(globals.project_path, "Content", "GUI", "quit.png")
            exit_b_img_path_h = os.path.join(globals.project_path, "Content", "GUI", "quit_hover.png")
            button_go.add_component(UIButton(button_go, exit_b_img_path, exit_b_img_path_h, globals.quit_event))
            return button_go

        elif enum is UIButtonProduct.PlayAgainButton:
            button_go = UIObject(gw, 735, 800)
            play_img = os.path.join(globals.project_path, "Content", "GUI", "play_again.png")
            play_img_hover = os.path.join(globals.project_path, "Content", "GUI", "play_again_hover.png")
            button_go.add_component(UIButton(button_go, play_img, play_img_hover, globals.play_again_event))
            return button_go

        elif enum is UIButtonProduct.BackButton:
            button_go = UIObject(gw, 850, 900)
            backb_img = os.path.join(globals.project_path, "Content", "GUI", "back.png")
            backb_h_img = os.path.join(globals.project_path, "Content", "GUI", "back_hover.png")
            button_go.add_component(UIButton(button_go, backb_img, backb_h_img, globals.back_event))
            return button_go

        elif enum is UIButtonProduct.HighScoreButton:
            button_go = UIObject(gw, 735, 400)
            highscore_img = os.path.join(globals.project_path, "Content", "GUI", "highscore.png")
            highscore_img_h = os.path.join(globals.project_path, "Content", "GUI", "highscore_hover.png")
            button_go.add_component(UIButton(button_go, highscore_img, highscore_img_h, globals.highscore_event))
            return button_go

        elif enum is UIButtonProduct.ControlsButton:
            button_go = UIObject(gw, 750, 500)
            controls_img = os.path.join(globals.project_path, "Content", "GUI", "controls.png")
            controls_img_h = os.path.join(globals.project_path, "Content", "GUI", "controls_hover.png")
            button_go.add_component(UIButton(button_go, controls_img, controls_img_h, globals.controls_event))
            return button_go


class BackGroundFactory(AbstractFactory):
    def CreateProduct(self, enum: UIBackground, game_world) -> UIObject:
        gw = game_world
        bg_go = UIObject(gw, 0, 0)

        if enum is UIBackground.MenuBackGround:
            _backGround_b_image = os.path.join(gw.project_dir, "Content", "GUI", "spaceBackGround.png")
            bg_go.add_component(ScrollingBackGround(bg_go, _backGround_b_image))
            return bg_go
        elif enum is UIBackground.EasyDiffBackground:
            _image = os.path.join(gw.project_dir, "Content", "GUI", "easydiff.jpg")
            bg_go.add_component(UIDecor(bg_go, _image))
            return bg_go
        elif enum is UIBackground.GameOverBackground:
            _image = os.path.join(gw.project_dir, "Content", "GUI", "overlay_black.png")
            bg_go.add_component(UIDecor(bg_go, _image))
            return bg_go


class UIDecorFactory(AbstractFactory):
    def CreateProduct(self, enum, game_world) -> UIObject:
        gw = game_world
        if enum is UIDecorProduct.GameOverText:
            go = UIObject(gw, 490, 50)
            gameover_img = os.path.join(gw.project_dir, "Content", "GUI", "gameover_display.png")
            go.add_component(UIDecor(go, gameover_img))
            return go

        elif enum is UIDecorProduct.HighScoreText:
            go = UIObject(gw, 490, 250)
            score_img = os.path.join(gw.project_dir, "Content", "GUI", "score_display.png")
            go.add_component(UIDecor(go, score_img))
            return go
