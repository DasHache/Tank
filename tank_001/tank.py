import Tkinter as Tk

class Tank:

    def __init__(self, world, x, y):
        self.world = world
        c = self.world.canvas
        self.x = x
        self.y = y
        self.s = 40
        
        #tank
        d = self.s/2
        tankx1 = x - d
        tanky1 = y - d
        tankx2 = x + d
        tanky2 = y + d
        c.create_rectangle(tankx1, tanky1, tankx2, tanky2, fill="red")

        #barrel
        bw = 4
        bx1 = tankx1 + (tankx2 - tankx1)/2
        by1 = tanky1 + (tanky2 - tanky1)/2
        bx2 = bx1 + 100
        by2 = by1 + bw
        c.create_rectangle(bx1, by1, bx2, by2, fill="grey")

        #charge
        ch_centerx = bx2
        ch_centery = by1 + bw/2
        chx1 = ch_centerx - 10
        chy1 = ch_centery - 10
        chx2 = ch_centerx + 10
        chy2 = ch_centery + 10
        ch = c.create_oval(chx1, chy1, chx2, chy2, fill="yellow")

        self.ch = ch 
