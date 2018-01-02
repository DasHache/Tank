import Tkinter as Tk

# v.0.2.0 - Adding a timer
# v.0.2.1 - Make a timer to repeat

root = Tk.Tk()

canvasw = 700
canvash = 500
w = Tk.Canvas(root, width=canvasw, height=canvash)
w.pack()

#canvas
w.create_rectangle(0, 0, canvasw, canvash, fill="light blue")

#base
basex1 = 0
basey1 = canvash - 300
basex2 = 100
basey2 = canvash
w.create_rectangle(basex1, basey1, basex2, basey2, fill="black")

#tank
tankx1 = 0 + 50
tanky1 = basey1 - 50
tankx2 = 0 + 100
tanky2 = basey1
w.create_rectangle(tankx1, tanky1, tankx2, tanky2, fill="red")

#barrel
bw = 4
bx1 = tankx1 + (tankx2 - tankx1)/2
by1 = tanky1 + (tanky2 - tanky1)/2
bx2 = bx1 + 100
by2 = by1 + bw
w.create_rectangle(bx1, by1, bx2, by2, fill="grey")

#charge
ch_centerx = bx2
ch_centery = by1 + bw/2
chx1 = ch_centerx - 10
chy1 = ch_centery - 10
chx2 = ch_centerx + 10
chy2 = ch_centery + 10
ch = w.create_oval(chx1, chy1, chx2, chy2, fill="yellow")


from threading import Timer
class RTimer:
    def __init__(self):
        pass
        
    def start(self):
        self.t = Timer(1.0, self.callback)
        self.t.start()
        
    def callback(self):
        w.move(ch, 10, 0)
        self.start()

rt = RTimer()
rt.start()

root.mainloop()


# next: make the charge movement traceable and defined by an equation!


