import Tkinter as Tk
import time

class Charge:

    def __init__(self, world, velocity, force, coord):
        self.c = world.canvas
        self.t = time.time()
        self.s = 10.
        self.v = velocity # m/s --- velocity tuple
        self.f = (0.,10.) # Newton --- force tuple
        self.xy = (100.,100.) # m --- coord tuple
        self.d = (0.,0.) # m --- coord. delta tuple
        self.o = self.c.create_oval(self.xy[0], self.xy[1], self.xy[0]+self.s, self.xy[1]+self.s, fill="yellow")

    def draw(self):
        # print 'charge-draw'
        self.c.move(self.o, self.d[0], self.d[1])
        p = self.c.coords(self.o)
        # print p
        self.c.create_oval(p[0], p[1], p[0]+2, p[1]+2, fill="gray")
        
    def recalc(self):
        # print 'charge-recalc'
        dt = self.gettime()
        dx = self.v[0] * dt 
        dy = 9.8 * dt * dt 
        self.d = (dx - self.d[0], dy - self.d[1])
        self.dxy = (dx, dy)

    def gettime(self):
        dt = time.time() - self.t
        # print dt
        return dt/10.

    def setSpeed(self, vx):
        self.v = (vx, self.v[1])
        
        
class Tank:

    def __init__(self, world, x, y):
        self.w = world
        self.c = world.canvas
        self.x = x
        self.y = y
        self.s = 40

    def draw(self):
        #tank
        d = self.s/2
        tankx1 = self.x - d
        tanky1 = self.y - d
        tankx2 = self.x + d
        tanky2 = self.y + d
        self.c.create_rectangle(tankx1, tanky1, tankx2, tanky2, fill="red")

        #barrel
        bw = 4
        bx1 = tankx1 + (tankx2 - tankx1)/2
        by1 = tanky1 + (tanky2 - tanky1)/2
        bx2 = bx1 + 100
        by2 = by1 + bw
        self.c.create_rectangle(bx1, by1, bx2, by2, fill="grey")

        #charge
        ch_centerx = bx2
        ch_centery = by1 + bw/2
        chx1 = ch_centerx - 10
        chy1 = ch_centery - 10
        chx2 = ch_centerx + 10
        chy2 = ch_centery + 10
        ch = self.c.create_oval(chx1, chy1, chx2, chy2, fill="yellow")

        self.ch = ch 

    def recalc(self):
        pass
