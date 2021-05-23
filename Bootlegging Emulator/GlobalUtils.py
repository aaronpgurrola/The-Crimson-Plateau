from enum import IntEnum

class Drugs(IntEnum):
    MJ = 1
    COKE = 2
    SHINE = 3

# Helper function to determine if number equal or between 0 and 1
def isPercentage(num: float):
    if num < 0 or num > 1:
        raise ValueError('Invalid number. Please input number between 0 and 1.')
        return False
    else:
        return True

def typeChecker(type: int):
    if type < 1 or type > 3:
        raise ValueError('Invalid type.')
        return False
    else:
        return True

def toCurrency(amount: float):
    return "${:,}".format(round(amount))
