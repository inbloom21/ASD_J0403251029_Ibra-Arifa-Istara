# Nama : Ibra Arifa Istara
# NIM : J0403251029
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Implementasi Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan seluruh kumpulan edge secara global berdasarkan bobot terkecil 
edges.sort()

mst = []
total_weight = 0

# Set sederhana untuk melacak node mana saja yang sudah terpilih 
connected = set()

# Proses perulangan untuk memeriksa setiap edge yang sudah terurut 
for weight, u, v in edges:
     
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight 
        connected.add(u)
        connected.add(v) 

# Menampilkan hasil akhir struktur MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot", total_weight)