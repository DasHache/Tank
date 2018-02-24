import Tkinter as Tk
from rtimer import BetterTimer

class World:

    def __init__(self):
        root = Tk.Tk()
        self.ground = root
        canvasw = 700
        canvash = 500
        self.canvas = Tk.Canvas(root, width=canvasw, height=canvash)
        self.canvas.pack()

        #canvas
        self.canvas.create_rectangle(0, 0, canvasw, canvash, fill="light blue")

        #base
        basex1 = 0
        basey1 = canvash - 300
        basex2 = 100
        basey2 = canvash
        self.canvas.create_rectangle(basex1, basey1, basex2, basey2, fill="black")

        
        #account the non-static objects
        self.objects = []

    def addTank(self, tank):
        self.objects.append(tank)
        
    def update(self):
        # objects, forces
        # for t in self.objects: 
        #     affect(t, force)
        print 'called world.update()'

    def run(self):

        # add timer to call self.update()
        timer = BetterTimer(self, "update")
        timer.start()

        # run the world
        self.ground.mainloop()


        
