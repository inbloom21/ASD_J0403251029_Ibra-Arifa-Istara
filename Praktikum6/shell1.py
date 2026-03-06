def shellSort(data):
    sublistcount = len(data) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(data, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", data)

        sublistcount = sublistcount // 2

def gapInsertionSort(data, start, gap):
    for i in range(start + gap, len(data), gap):
        currentvalue = data[i]
        position = i

        while position >= gap and data[position - gap] > currentvalue:
            data[position] = data[position - gap]
            position = position - gap

        data[position] = currentvalue

data = [21, 87, 55, 43, 32, 86, 3, 2]
shellSort(data)
print(data)