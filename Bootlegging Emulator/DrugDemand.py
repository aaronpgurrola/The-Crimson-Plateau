# Needed for drug types
import GlobalUtils as gu

# Constants for minimum & maximum demand
MINIMUM_DEMAND = .01
MAXIMUM_DEMAND = 1

# Class for Drug Demand
# Used to return current demands by type
# Used to alter demand by type
class DrugDemand:
    def __init__(self):
        self.demandDict = {gu.Drugs.COKE: 0.5, gu.Drugs.MJ: 0.5, gu.Drugs.SHINE: 0.5}

    # Getter method

    # Return demand by type
    def getDrugDemand(self, type: int):
        if gu.typeChecker(type):
            return self.demandDict[type]

    # Alteration methods
    # Reduction methods

    # Utility to determine if demand can be reduced
    # Utility for reduceDrugDemand
    def canReduce(self, type: int, percentage: float):
        if not gu.isPercentage(percentage):
            pass
        if (self.getDrugDemand(type)-percentage) < MINIMUM_DEMAND:
            return False
        else:
            return True

    # Reduces drug demand by percentage 0 to 1
    # Uses canReduce helper method
    def reduceDrugDemand(self, type: int, percentage: float):
        if not gu.isPercentage(percentage):
            pass
        if canReduce(type, percentage):
            self.demandDict[type] = self.demandDict[type] - percentage
        else:
            self.demandDict[type] = MINIMUM_DEMAND

    # Increase methods
    # Utility to determine if demand can be increased
    # Utility for increaseDrugDemand
    def canIncrease(self, type: int, percentage: float):
        if not gu.isPercentage(percentage):
            pass
        if (self.getDrugDemand(type) + percentage) > MAXIMUM_DEMAND:
            return False
        else:
            return True

    # Reduces drug demand by percentage 0 to 1
    # Uses canReduce helper method
    def increaseDrugDemand(self, type: int, percentage: float):
        if not gu.isPercentage(percentage):
            pass
        if canIncrease(self.demandDict[type], percentage):
            self.demandDict[type] = self.demandDict[type] + percentage
        else:
            self.demandDict[type] = MAXIMUM_DEMAND
