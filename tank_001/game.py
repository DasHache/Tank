from tank import Tank
from rtimer import RTimer
from handle import *
from world import World

w = World()

t = Tank(w, 100, 100)
t2 = Tank(w, 100, 200)

rt = RTimer(w, t)
rt.start()
rt2 = RTimer(w, t2)
rt2.start()


w.run()



