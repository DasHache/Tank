import Tkinter as Tk
from rtimer import BetterTimer
from tank import Tank, Charge
from time import sleep

class World:

    def __init__(self):
        root = Tk.Tk()
        self.ground = root
        canvasw = 700
        canvash = 500
        self.canvas = Tk.Canvas(root, width=canvasw, height=canvash)
        self.canvas.pack()

        #canvas
        self.canvas.create_rectangle(0, 20, canvasw, canvash, fill="light blue")

        #base
        basex1 = 0
        basey1 = canvash - 300
        basex2 = 100
        basey2 = canvash
        self.canvas.create_rectangle(basex1, basey1, basex2, basey2, fill="black")
        
        #account the non-static objects
        self.objects = []

    def addTank(self):
        t = Tank(self, 100, 100)
        self.objects.append(t)

    def addCharge(self):
        o = Charge(self, (0,0), (0,0), (0,0))
        self.objects.append(o)

    def update(self):
        print 'w-up'
        z = self.canvas.create_oval(15, 5, 25, 15, fill="red")
        sleep(0.1) # 100 ms
        self.canvas.delete(z)

        # Re-calculate: objects, forces, velocity
        for o in self.objects: 
            o.recalc()
            


    def draw(self):
        print 'w-draw'
        z = self.canvas.create_oval(5, 5, 15, 15, fill="black")
        sleep(0.1) # 100 ms
        self.canvas.delete(z)
        
        for o in self.objects:
            o.draw()

        
    def run(self):

        # add timer to call self.update()
        timerUpdate = BetterTimer(self, "update", 0.1)
        timerUpdate.start()

        # add timer to call self.draw()
        timerDraw = BetterTimer(self, "draw", 0.1)
        timerDraw.start()

        # run the world
        self.ground.mainloop()


        
