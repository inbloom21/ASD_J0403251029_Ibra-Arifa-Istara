# Nama : Ibra Arifa Istara
# NIM : J0403251029
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree

import heapq

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

mst, total = prim(graph, 'A') # gunakan A sebagai titik awal

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)