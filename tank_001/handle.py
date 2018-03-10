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

        elif event.char == u'w':
            self.w.changeBarrelAngle(+5)
        elif event.char == u's':
            self.w.changeBarrelAngle(-5)

        elif event.char == u'q':
            self.w.powerUp()
        elif event.char == u'a':
            self.w.powerDown()
        else:
            print "undefined action"

        self.w.updateLabels()

    def mouse_function(self, event):
        self.canvas.focus_set()
        print "clicked at", event.x, event.y

