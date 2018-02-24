from tank import Tank
from rtimer import RTimer
from handle import *
from world import World


class Game:

    def __init__(self):
        pass

    def start(self):
        w = World()
        #t = Tank(w, 100, 100)
        #rt = RTimer(w, t)
        #rt.start()
        w.run()



game = Game()
game.start()
