class Handle:

    def __init__(self, canvas_, tank_):
        self.canvas = canvas_
        self.canvas.bind("<Button-1>", self.mouse_function)
        self.canvas.bind("<Key>", self.key_function)
        self.tank = tank_

    def key_function(self, event):
        #print "pressed", repr(event.char)
        if event.char == u'\uf700':
            self.move(self.tank.ch, 0, -10)
        else:
            self.move(self.tank.ch, 0, 10)


    def mouse_function(self, event):
        self.canvas.focus_set()
        print "clicked at", event.x, event.y

