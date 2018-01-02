import Tkinter as Tk

# v.0.1.2

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


root.mainloop()


# current version is v.0.1.2
# to get to v.0.1.3:
# 1. draw the barrel (long narrow rectangular in the middle of the tank)
# 2. add keyboard handler




