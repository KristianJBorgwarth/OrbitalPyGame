from typing import Type

from overrides import overrides

from DesignPatterns.FactoryPattern import AbstractFactory
from DesignPatterns.SingletonPattern import AbstractSingleton
from UI.UIComponents import UIButton
from UI.UIObjects import UIObject
from enum import Enum


class UIProduct(Enum):
    StartButton = 1,
    ExitButton = 2,
    HighScoreButton = 3,
    PlayAgainButton = 4


class ButtonFactory(AbstractFactory, AbstractSingleton):
    def __init__(self):
        pass

    @overrides
    def CreateProduct(self, event, enum: UIProduct) -> Type[UIObject]:
        button_go = UIObject
        if enum is UIProduct.StartButton:
            start_img_path = "Content/GUI/play.png"
            start_img_path_h = "Content/GUI/play_hover.png"
            button_go.add_component(UIButton(button_go, start_img_path, start_img_path_h, event))
            return button_go

        elif enum is UIProduct.ExitButton:
            return button_go

        elif enum is UIProduct.HighScoreButton:
            return button_go

        elif enum is UIProduct.PlayAgainButton:
            return button_go
