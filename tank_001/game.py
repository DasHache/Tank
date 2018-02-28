from tank import Tank
from rtimer import RTimer
from handle import *
from world import World


class Game:

    def __init__(self):
        self.w = World()
        self.h = Handle(self.w)

    def start(self):
        self.w.run()


game = Game()
game.start()
