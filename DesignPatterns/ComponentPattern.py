from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, owner_go):
        self.owner = owner_go

    def update(self):
        pass

    @abstractmethod
    def serialize(self):
        return {'type': self.__class__.__name__}

    @classmethod
    @abstractmethod
    def deserialize(cls, d: dict, owner_go) -> 'Component':
        pass
