﻿from abc import ABC, abstractmethod
from typing import Any


class AbstractFactory(ABC):
    @abstractmethod
    def CreateProduct(self, enum, game_world) -> Any:
        pass
