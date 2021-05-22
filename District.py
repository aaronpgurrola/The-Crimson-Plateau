from enum import Enum
import Front as f
import DrugDemand as dd
import GlobalUtils as gu
import DrugRun as dr
import time
import math

# Constants for different drug price constants
GALLON_PRICE = 5.0
MJ_GRAM_PRICE = 10.0
COKE_GRAM_PRICE = 20.0


# District is currently the top-tier component
# TODO: Build Map class to hold multiple districts
# TODO: Build methods to interact with other districts
class District():
    def __init__(self):
        # Each district will have independent drug demand
        self.drugDemand = dd.DrugDemand()

        # TODO: Whem Map class is built, move to Map class
        self.drugRun = dr.DrugRun()

        # List of front objects
        self.fronts = []

        # Determines whether or not every front is controlled by user
        # TODO: Create methods to determine if District is monopolized
        self.monopolized = False

    # Builds a front using the Front class
    # Appends it to a list of fronts in the District
    def createFront(self, name: str, base: float):
        front = f.Front(name, base)
        self.fronts.append(front)

    # Utility to print fronts and all their individual variables
    def printFronts(self):
        frontString = ''
        for front in self.fronts:
            newline = front.getName() + '\t' + str(front.getBase()) + '\t' + str(front.getHit())
            frontString+= newline + '\n'
        print(frontString)

    # Sets all fronts as not hit during drug run
    # TODO: When Map class is built, move to Map class
    def resetFronts(self):
        for front in self.fronts:
            front.resetHit()

    # Starts drug run
    # TODO: When Map class is built, move to Map class
    def startRun(self, type: int, quantity: int):
        self.resetFronts()
        self.drugRun.run(type, quantity)

    # Ends drug run
    # TODO: When Map class is built, move to Map class
    def endRun(self):
        self.resetFronts()
        self.drugRun.end()

    # Helper function for hitFront
    # Helper function to determine output $ of front.basew * demand%
    def demandFunction(self, type: int):
        return (1+(1/math.exp(5))) - math.exp(-5*self.drugDemand.getDrugDemand(type))

    # Hits a front and returns dollar amount
    # Used for testing
    # TODO: Check if front is owned
    def hitFrontByIndex(self, index: int):
        if self.drugRun.isRunning():
            self.fronts[index].hitFront()
            self.fronts[index].getBase()*self.demandFunction(demand)

def go():
    district = District()
    district.createFront("Store1", 0.5)
    district.createFront("Store2", 0.5)
    district.createFront("Store3", 0.4)
    district.createFront("Store4", 1.0)
    district.createFront("Store5", 0.6)
    district.createFront("Store6", 0.7)
    district.printFronts()

    start = time.time()
    elapsed = 0
    seconds = 20
    while elapsed < seconds:
        print(district.demandFunction(elapsed/seconds))
        elapsed = math.floor(time.time() - start)
        time.sleep(1)
        print(elapsed)

go()
