# Nama : Ibra Arifa Istara
# NIM : J0403251029
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree

import heapq

# data hubungan gedung dan bobotnya
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):

    # inisialisasi set untuk menyimpan node yang sudah dikunjungi
    visited = set([start])

    # inisialisasi heap untuk menyimpan edge yang akan diproses.
    edges = []
    
    # menambahkan semua edge dari node awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    # inisialisasi list untuk menyimpan edge yang termasuk dalam MST dan variabel untuk total bobot
    mst = []
    total_weight = 0
    
    # jalankan loop selama masih ada edge yang bisa diproses
    while edges:
        weight, u, v = heapq.heappop(edges) # mengambil edge dengan bobot terkecil
        
        # jika node tujuan belum dikunjungi, tambahkan ke MST dan update total bobot
        if v not in visited:

            visited.add(v)
            
            mst.append((u, v, weight))
            total_weight += weight
            
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

mst, total = prim(graph, 'A')

print("Edge yang dipilih:")

for edge in mst:
    print(edge)

print("Total biaya minimum =", total)

# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
# Jawab: Algoritma yang digunakan adalah algoritma Prim.

# 2. Edge mana saja yang dipilih?
# Jawab: Edge yang dipilih adalah AC dengan bobot 2, CD dengan bobot 1, dan DB dengan bobot 3.

# 3. Berapa total biaya minimum?
# Jawab: Total biaya minimum adalah 6.

# 4. Mengapa MST cocok digunakan pada kasus ini?
# Jawab: Karena kita ingin mencari biaya pemasangan kabel serendah mungkin, sehingga MST cocok digunakan.