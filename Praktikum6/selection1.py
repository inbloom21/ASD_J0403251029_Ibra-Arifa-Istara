def selectionSort(data):
    for fillslot in range(len(data)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if data[location] > data[positionOfMax]:
                positionOfMax = location

        # Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp

data = [33, 41, 53, 23, 51, 75, 34, 642]
selectionSort(data)
print(data)