from Tkinter import *

root = Tk()
#w = Label(root, text="Hello, im tank!")


canvas = Canvas(root, width=500, height=500)



x0 = 200
y0 = 300
x1 = 500
y1 = 200
r = canvas.create_rectangle(x0, y0, x1, y1, fill='blue')
r = canvas.create_rectangle(100, 100, 200, 400, fill='red')
w = canvas.create_line(15, 25, 200, 25)
# dash for _ _ _ _

#dasha for @*#$%@#$%*@#$%

#w.pack()
canvas.pack()
root.mainloop()

