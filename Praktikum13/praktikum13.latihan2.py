# Nama : Ibra Arifa Istara
# NIM : J0403251029
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()

for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
# Jawab: Edge yang menghubungkan node C dan D dengan bobot 1. Karena bobotnya paling kecil.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# Jawab: Karena pada algoritma Kruskal, edge akan disortir dari yang paling kecil terlebih dahulu, lalu edge yang paling kecil akan dipilih.

# 3. Berapa total bobot MST yang dihasilkan?
# Jawab: Total bobot MST yang dihasilkan adalah 6.

# 4. Mengapa edge tertentu tidak dipilih?
# Jawab: Edge tertentu tidak dipilih karena kedua node yang dihubungkan oleh edge tersebut sudah terhubung dan akan membentuk cycle jika dihubungkan.