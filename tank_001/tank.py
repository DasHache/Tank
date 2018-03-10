import Tkinter as Tk
import time
from math import sin, cos, pi

class Charge:

    def __init__(self, world, velocity, coords):
        self.c = world.canvas
        self.t = time.time()
        self.s = 10.
        self.v = velocity # m/s --- velocity tuple
        self.xy = coords # m --- coord tuple
        self.d = (0.,0.) # m --- coord. delta tuple
        z = self.s/2.
        self.o = self.c.create_oval(self.xy[0]-z, self.xy[1]-z, self.xy[0]+z, self.xy[1]+z, fill="yellow")

    def draw(self):
        # print 'charge-draw'
        self.c.move(self.o, self.d[0], self.d[1])
        p = self.c.coords(self.o)
        x = p[0] + self.s /2.
        y = p[1] + self.s /2.
        # print p
        
        self.c.create_oval(x-1, y-1, x+1, y+1, fill="gray")
        
    def recalc(self):
        # print 'charge-recalc'
        dt = self.gettime()
        dx = self.v[0] * dt 
        dy = self.v[1] * dt + 9.8 * dt * dt 
        self.d = (dx - self.d[0], dy - self.d[1])
        self.dxy = (dx, dy)

    def gettime(self):
        dt = time.time() - self.t
        # print dt
        return dt #/10.

    def setSpeed(self, vx):
        self.v = (vx, self.v[1])
        
        
class Tank:

    def __init__(self, world, x, y):
        self.w = world
        self.c = world.canvas
        self.x = x
        self.y = y
        self.s = 40
        self.bangle = 0
        self.blen = 50
        self.b = None
        
    def draw(self):
        #tank
        d = self.s/2
        tankx1 = self.x - d
        tanky1 = self.y - d
        tankx2 = self.x + d
        tanky2 = self.y + d
        self.c.create_rectangle(tankx1, tanky1, tankx2, tanky2, fill="red")

        #barrel
        self.bx = tankx1 + (tankx2 - tankx1)/2
        self.by = tanky1 + (tanky2 - tanky1)/2
        self.drawBarrel()

    def recalc(self):
        pass
        
    def calcBarrelEndPos(self):
        bdx = self.blen * cos(pi/180 * self.bangle)
        bdy = self.blen * sin(pi/180 * self.bangle)
        self.bx2 = self.bx + bdx
        self.by2 = self.by - bdy

    def drawBarrel(self):
        if self.b:
            self.c.delete(self.b)
            
        self.calcBarrelEndPos()
        self.b = self.c.create_line(self.bx, self.by, self.bx2, self.by2, fill="grey", width=3)

    def getBarrelEndPos(self):
        return (self.bx2, self.by2)

    def changeBarrelAngle(self, dalpha=5):
        if dalpha > 0:
            if (self.bangle + dalpha) <= 90:
                self.bangle += dalpha
        else:
            if (self.bangle + dalpha) >= 0:
                self.bangle += dalpha
        
    def getBarrelAngle(self):
        return self.bangle
        
