# Nama : Ibra Arifa Istara
# NIM : J0403251029
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree

# Kasus 1: Jaringan Jalan Antar Kota

import heapq

graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Bogor': 2, 'Jakarta': 3, 'Bandung': 4},
    'Jakarta': {'Bogor': 5, 'Depok': 3, 'Bandung': 6},
    'Bandung': {'Depok': 4, 'Jakarta': 6}
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

mst, total = prim(graph, 'Depok') # gunakan Depok sebagai titik awal

print("MST:")

for edge in mst:
    print(edge)

print("Total bobot minimum =", total)

# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
# Jawab: Kasus yang dipilih adalah Kasus 1: Jaringan Jalan Antar Kota.

# 2. Algoritma apa yang digunakan?
# Jawab: Algoritma yang digunakan adalah algoritma Prim.

# 3. Edge mana saja yang dipilih dalam MST?
# Jawab: Edge yang dipilih dalam MST adalah Depok-Bogor dengan bobot 2, Depok-Jakarta dengan bobot 3, dan Depok-Bandung dengan bobot 4.

# 4. Berapa total bobot MST?
# Jawab: Total bobot MST adalah 9.

# 5. Mengapa edge tertentu tidak dipilih?
# Jawab: Karena ada edge dengan bobot yang lebih kecil yang menghubungkan node yang sama.