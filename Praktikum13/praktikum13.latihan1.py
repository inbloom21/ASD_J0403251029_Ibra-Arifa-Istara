# Nama : Ibra Arifa Istara
# NIM : J0403251029
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# Jawab: Jumlah edge pada graph awal adalah 5, sedangkan pada spanning tree adalah 3.
# 
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# Jawab: Karena ketentuan dari sebuah tree adalah tidak boleh memiliki cycle.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
# Jawab: Karena spanning tree hanya menghubungkan semua vertex dengan jumlah edge minimum, sehingga tidak boleh ada edge yang berlebihan yang dapat menyebabkan cycling.