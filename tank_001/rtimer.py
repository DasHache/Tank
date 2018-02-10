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
