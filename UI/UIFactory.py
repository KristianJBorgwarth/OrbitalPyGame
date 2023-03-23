import os
import pygame
import globals
from Scripts.DesignPatterns.FactoryPattern import AbstractFactory
from UI.UIComponents import UIButton, BackGround
from UI.UIObjects import UIObject
from enum import Enum


class UIProduct(Enum):
    StartButton = 1
    ExitButton = 2
    HighScoreButton = 3
    PlayAgainButton = 4


class UIBackground(Enum):
    MenuBackGround = 1
    EasyDiffBackground = 2
    HardDiffBackground = 3
    BossDiffBackground = 4


class ButtonFactory(AbstractFactory):

    def __init__(self):
        globals.start_event = pygame.USEREVENT + 1
        pygame.event.set_allowed(pygame.USEREVENT + 1)
        globals.quit_event = pygame.USEREVENT + 2
        pygame.event.set_allowed(globals.quit_event)

    def CreateProduct(self, enum: UIProduct, game_world) -> UIObject:
        gw = game_world
        if enum is UIProduct.StartButton:
            button_go = UIObject(gw, 825, 300)
            start_img_path = os.path.join(globals.project_path, "Content", "GUI", "play.png")
            start_img_path_h = os.path.join(globals.project_path, "Content", "GUI", "play_hover.png")
            button_go.add_component(UIButton(button_go, start_img_path, start_img_path_h, globals.start_event))
            return button_go

        elif enum is UIProduct.ExitButton:
            button_go = UIObject(gw, 845, 400)
            exit_b_img_path = os.path.join(globals.project_path, "Content", "GUI", "quit.png")
            exit_b_img_path_h = os.path.join(globals.project_path, "Content", "GUI", "quit_hover.png")
            button_go.add_component(UIButton(button_go, exit_b_img_path, exit_b_img_path_h, globals.quit_event))
            return button_go

        elif enum is UIProduct.HighScoreButton:
            pass

        elif enum is UIProduct.PlayAgainButton:
            pass


class BackGroundFactory(AbstractFactory):
    def CreateProduct(self, enum: UIBackground, game_world) -> UIObject:
        gw = game_world

        if enum is UIBackground.MenuBackGround:
            bg_go = UIObject(gw, 0, 0)
            _backGround_b_image = os.path.join(gw.project_dir, "Content", "GUI", "spaceBackGround.png")
            bg_go.add_component(BackGround(bg_go, _backGround_b_image))
            return bg_go
