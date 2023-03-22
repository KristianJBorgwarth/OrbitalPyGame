from abc import ABC, abstractmethod
from typing import Any

import pygame


class Component(ABC):
    def __init__(self, owner_go):
        self.owner = owner_go

    def update(self):
        pass

    def serialize(self):
        return {'type': self.__class__.__name__}

    @classmethod
    def deserialize(cls, d: dict, owner_go) -> Any:
        pass
