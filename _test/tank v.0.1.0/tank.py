import Tkinter as Tk


root = Tk.Tk()

w = Tk.Canvas(root, width=700, height=700)
w.pack()

w.create_rectangle(50, 50, 600, 400, fill="blue")

w.create_line(0, 10, 640, 10)
w.create_line(10, 0, 10, 440, fill="red", dash=(4, 4))



root.mainloop()


# current version is v.0.1.0
# to make v.0.1.1 do the following
# 1. add variables for the coordinates of the canvas
# 2. adjust canvas' size
# 3. draw a square for a base



