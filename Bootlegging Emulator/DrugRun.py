import GlobalUtils as gu

# DrugRun class is currently a component of District
# TODO: When district testing is finished, make DrugRun a component of map
class DrugRun():
    def __init__(self):
        self.running = False
        self.runType = 1
        self.quantity = 0
        self.haul = 0

    def setRunType(self, type: int):
        if gu.typeChecker(type):
            self.runType = type

    def getRunType(self):
        return self.runType

    def getQuantity(self):
        return self.quantity

    def run(self, type: int, quantity: int):
        self.setRunType(type)
        self.quantity = quantity
        self.running = True

    def end(self):
        print(self.haul)
        self.running = False
        self.haul = 0
        self.quantity = 0

    def addToHaul(self, money: float):
        self.haul += money

    def getCurrentHaul(self):
        return self.haul

    def isRunning(self):
        return self.running
