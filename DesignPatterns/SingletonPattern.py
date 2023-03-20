from abc import ABC, abstractmethod


class AbstractSingleton(ABC):

    __instance = None

    @abstractmethod
    def __init__(self):
        pass

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super.__new__(cls)
        return cls.__instance

