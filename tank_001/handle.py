class Handle:

    def __init__(self, world):
        self.canvas = world.canvas
        self.canvas.bind("<Button-1>", self.mouse_function)
        self.canvas.bind("<Key>", self.key_function)
        self.w = world

    def key_function(self, event):
        #print "pressed", repr(event.char)
        if event.char == u'1':
            print "add new tank"
            self.w.addTank()
        elif event.char == u'2':
            print "add a charge...!"
            self.w.addCharge()
        else:
            print "undefined action"


    def mouse_function(self, event):
        self.canvas.focus_set()
        print "clicked at", event.x, event.y

