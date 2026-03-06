def selectionSort(data):
    for fillslot in range(len(data)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if data[location] < data[positionOfMax]:
                positionOfMax = location

        # Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp

# mengurutkan data dari tertinggi ke terendah dengan selection sort
nilai = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
selectionSort(nilai)

# mengambil 5 skor dengan nilai tertinggi
kandidat = 1
nilaiKandidat = []
for i in nilai:
    if kandidat <= 5:
        nilaiKandidat.append(i)
        kandidat += 1
    else:
        break

print(f"Skor 5 kandidat dengan nilai tertinggi adalah {nilaiKandidat}")