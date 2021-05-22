
class Front:
    def __init__(self, name: str, base: float):
        self.name = name
        self.base = base
        self.hit = False

    def upgrade(self):
        self.base += 0.1

    def getName(self):
        return self.name

    def getBase(self):
        return self.base

    def hitFront(self):
        self.hit = True

    def resetHit(self):
        self.hit = False

    def getHit(self):
        return self.hit
