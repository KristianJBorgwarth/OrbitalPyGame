from abc import ABC, abstractmethod


class IState(ABC):
    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def exit(self):
        pass


class StateMachine:
    def __init__(self):
        self.currentState = None

    def start_statemachine(self, startingState: IState):
        startingState.enter()

    def change_state(self, newState: IState):
        if newState is self.currentState: return
        self.currentState.exit()
        self.currentState = newState
        self.currentState.enter()
