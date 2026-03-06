def insertionSort(data):
    for index in range(1, len(data)):
        currentvalue = data[index]
        position = index

        while position > 0 and data[position - 1] < currentvalue:
            data[position] = data[position - 1]
            position = position - 1
            data[position] = currentvalue

data = [32, 45, 12, 75, 42, 23, 52, 3, 6, 23]
insertionSort(data)
print(data)