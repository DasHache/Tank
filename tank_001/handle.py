class Handle:

    def __init__(self, world):
        self.canvas = world.canvas
        self.canvas.bind("<Button-1>", self.mouse_function)
        self.canvas.bind("<Key>", self.key_function)
        self.w = world

    def key_function(self, event):
        #print "pressed", repr(event.char)
        if event.char == u'a':
            print "add new tank"
            self.w.addTank()
        else:
            print "undefined action"


    def mouse_function(self, event):
        self.canvas.focus_set()
        print "clicked at", event.x, event.y

