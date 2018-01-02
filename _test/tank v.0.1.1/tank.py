import Tkinter as Tk

root = Tk.Tk()

canvasw = 700
canvash = 500
w = Tk.Canvas(root, width=canvasw, height=canvash)
w.pack()

w.create_rectangle(0, 0, canvasw, canvash, fill="light blue")
w.create_rectangle(100, 100, 200, 300, fill="black")


root.mainloop()


# current version is v.0.1.1
# to make v.0.1.2 do the following:
# 1. add variables for the base coordinates
# 2. place the base at the bottom left corner
# 3. draw a tank (rectangle) on top of the base



