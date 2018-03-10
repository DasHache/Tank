import Tkinter as Tk
from rtimer import BetterTimer
from tank import Tank, Charge
from time import sleep
from math import sin,cos,pi



class World:

    def __init__(self):

        root = Tk.Tk()
        self.ground = root
        canvasw = 1000
        canvash = 600
        self.canvas = Tk.Canvas(root, width=canvasw, height=canvash)
        self.canvas.pack()

        #canvas
        self.canvas.create_rectangle(0, 20, canvasw, canvash, fill="light blue")

        #base
        basex1 = 0
        basey1 = canvash - 100
        basex2 = 100
        basey2 = canvash
        self.canvas.create_rectangle(basex1, basey1, basex2, basey2, fill="black")

        #
        self.v = 5
        self.a = 0

        self.lpn = Tk.Label(root, text="Power: ")
        self.lpn.pack()

        self.svp = Tk.StringVar()
        self.lpv = Tk.Label(root, textvariable=self.svp)
        self.lpv.pack()

        self.lan = Tk.Label(root, text="Angle: ")
        self.lan.pack()

        self.sva = Tk.StringVar()
        self.lav = Tk.Label(root, textvariable=self.sva)
        self.lav.pack()

        # self.e = Tk.Entry(root)
        # self.e.bind('<Return>', self.speedOnEnter)
        # self.e.pack()
        # self.b = Tk.Button(root, text="get", width=10, command=self.readSpeed)
        # self.b.pack()

        #account the non-static objects
        self.objects = []

    # def speedOnEnter(self, e):
    #     x = e.widget.get()
    #     print x
    #     v_ = int(x)
    #     self.v = v_
        
    # def readSpeed(self):
    #     v_ = int(self.e.get())
    #     print v_
    #     self.v = v_

    def updateLabels(self):
        self.svp.set(str(self.v))
        self.sva.set(str(self.t.getBarrelAngle()))

    def addTank(self):
        self.t = Tank(self, 100, 500)
        self.objects.append(self.t)

    def addCharge(self):
        startPos = self.t.getBarrelEndPos()
        balpha = self.t.getBarrelAngle()
        vx =  self.v * cos(pi/180 * balpha)
        vy = -self.v * sin(pi/180 * balpha)
        o = Charge(self, (vx, vy), startPos)
        self.objects.append(o)

    def powerUp(self):
        if self.v <= 100:
            self.v +=5

    def powerDown(self):
        if self.v >=5:
            self.v -=5

    def changeBarrelAngle(self, da):
        self.t.changeBarrelAngle(da)
        
    def update(self):
        # print 'w-up'            
        z = self.canvas.create_oval(15, 5, 25, 15, fill="red")
        sleep(0.1) # 100 ms
        self.canvas.delete(z)

        # Re-calculate: objects, forces, velocity
        for o in self.objects: 
            o.recalc()
            
    def draw(self):
        # print 'w-draw'
        z = self.canvas.create_oval(5, 5, 15, 15, fill="black")
        sleep(0.1) # 100 ms
        self.canvas.delete(z)
        
        for o in self.objects:
            o.draw()

        
    def run(self):
        # add timer to call self.update()
        self.timerUpdate = BetterTimer(self, self, "update", 0.5)
        self.timerUpdate.start()

        # add timer to call self.draw()
        self.timerDraw = BetterTimer(self, self, "draw", 0.5)
        self.timerDraw.start()

        # run the world
        self.ground.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.ground.mainloop()

    def on_closing(self):
        self.timerUpdate.stop()
        self.timerDraw.stop()
        sleep(2)

        # self.ground.destroy()   
        exit()


        
