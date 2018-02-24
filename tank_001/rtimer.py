from threading import Timer

class RTimer:
    def __init__(self, world, tank):
        self.world = world
        self.tank = tank

    def start(self):
        self.t = Timer(1.0, self.callback)
        self.t.start()

    def callback(self):
        self.world.canvas.move(self.tank.ch, 10, 0)
        self.start()



class BetterTimer:
    def __init__(self, obj, obj_method_name):
        self.o = obj
        self.omn = obj_method_name

    def start(self):
        self.t = Timer(1.0, self.callback)
        self.t.start()

    def callback(self):
        getattr(self.o, self.omn)()
        self.start()
        
