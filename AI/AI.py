import time

from Components import Rigidbody
import pygame.math
class BotState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print('Current:', self, ' => switched to new state', state.name)
            self.__class__ = state
        else:
            print('Current:', self, ' => switching to', state.name, 'not possible.')

    def __str__(self):
        return self.name


class Off(BotState):
    name = "off"
    allowed = ['on', 'move']


class On(BotState):
    """ State of being powered on and working """
    name = "on"
    allowed = ['off', 'move', 'suspend', 'hibernate']
class Move(BotState):
    name = "move"
    allowed = ['off', 'move', 'suspend', 'hibernate']


class Suspend(BotState):
    """ State of being in suspended mode after switched on """
    name = "suspend"
    allowed = ['on', 'move']


class Hibernate(BotState):
    """ State of being in hibernation after powered on """
    name = "hibernate"
    allowed = ['on', 'move']


class Bot(object):


    def __init__(self, model='Test'):
        self.model = model
        # State of the computer - default is off.
        self.state = Off()

    def change(self, state):
        """ Change state """
        self.state.switch(state)
    def change(self, state):
        """ Change state """
        self.state.switch(state)

    def update (self, rigidbody, world):
        if self.state.name != 'move':
            self.change(Move)

        if self.state.name == 'move':
            rigidbody.update_AI_velocity('y', world.delta_time)


            print(rigidbody.velocity)
        # if
        #self.change(On)
        # if
        #self.change(Off)
        # if
        #self.change(On)
        # if
        #self.change(Suspend)
        # if
        #self.change(Hibernate)
        # if
        #self.change(On)
        # if
        #self.change(Off)

