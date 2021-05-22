import District as d
import time

def go():
    district = d.District()
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
