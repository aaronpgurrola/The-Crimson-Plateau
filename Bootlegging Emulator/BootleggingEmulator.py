import District as d
import GlobalUtils as gu
import time
import math

def go():
    district = d.District()
    district.createFront("Store1", 0.5)
    district.createFront("Store2", 0.5)
    district.createFront("Store3", 0.4)
    district.createFront("Store4", 1.0)
    district.createFront("Store5", 0.6)
    district.createFront("Store6", 0.7)
    district.ownFrontByIndex(0)
    district.ownFrontByIndex(2)
    district.ownFrontByIndex(3)
    district.ownFrontByIndex(5)
    district.printFronts()
    district.drugRun.run(gu.Drugs.MJ, 50)
    start = time.time()
    elapsed = 0
    seconds = 10
    while elapsed < seconds:
        elapsed = math.floor(time.time() - start)
        time.sleep(1)
        if elapsed == 3:
            district.hitFrontByIndex(0)
        if elapsed == 4:
            district.hitFrontByIndex(5)
        if elapsed == 5:
            district.hitFrontByIndex(3)
        if elapsed == 8:
            district.hitFrontByIndex(2)
        print(elapsed)
        district.printFronts()
    district.drugRun.end()
go()
