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
    def __init__(self, w, obj, obj_method_name, dt=1):
        self.done = False
        self.world = w
        self.o = obj
        self.omn = obj_method_name
        self.dt = dt

    def start(self):
        if self.done:
            return
        # print '666'
        self.t = Timer(self.dt, self.callback)
        self.t.start()

    def callback(self):
        getattr(self.o, self.omn)()
        self.start()

    def stop(self):
        print '2'
        self.t.cancel()
        self.done = True
