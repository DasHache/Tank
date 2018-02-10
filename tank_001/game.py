from tank import Tank
from rtimer import RTimer
from handle import *
from world import World

w = World()

t = Tank(w, 100, 100)

rt = RTimer(w, t)
rt.start()


w.run()



