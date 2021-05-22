class Drugs(Enum):
    MJ = 1
    COKE = 2
    BLUE = 3

def typeChecker():
    if type < 1 or type > 3:
        raise ValueError('Invalid type.')
        return False
    else:
        return True

def toCurrency(amount: float):
    return "${:,}".format(round(amount))
