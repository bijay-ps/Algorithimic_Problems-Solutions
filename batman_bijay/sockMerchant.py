def noOfSocksPairs(ar):
    socksHashTable = {}
    for item in ar:
        socksHashTable.update({item: ar.count(item)})
    totalPairs = 0
    for val in socksHashTable.values():
        if (val > 2):
            if (val % 2 == 0):
                totalPairs = totalPairs + (val / 2)
            if (val % 2 != 0):
                extraSocks = val % 2
                pair = (val - extraSocks) / 2
                totalPairs = totalPairs + pair
        elif (val == 2):
            totalPairs += 1
    return int(totalPairs)


testArr1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
testArr2 = [1, 2, 1, 2, 1, 3, 2]

print(noOfSocksPairs(testArr1))
print(noOfSocksPairs(testArr2))
