import GlobalUtils as gu

class Front:
    def __init__(self, name: str, base: float):
        if not gu.isPercentage(base):
            pass
        self.name = name
        self.base = base
        self.hit = False
        self.owned = False

    def __str__(self):
        own = ''
        if self.owned:
            own = 'IS OWNED'
        else:
            own = 'IS NOT OWNED'
        hit = ''
        if self.hit:
            hit = 'HAS BEEN HIT'
        else:
            hit = 'HAS NOT BEEN HIT'
        return f'{self.name}\t{self.base}\t{own} AND {hit}'

    def upgrade(self):
        self.base += 0.1

    def getName(self):
        return self.name

    def getBase(self):
        return self.base

    def hitFront(self):
        if self.owned:
            self.hit = True

    def resetHit(self):
        self.hit = False

    def isHit(self):
        return self.hit

    def own(self):
        self.owned = True

    def disOwn(self):
        self.owned = False

    def isOwned(self):
        return self.owned
