# Nama : Ibra Arifa Istara
# NIM : J0403251029
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path

import heapq

# buat graph dengan bobot untuk setiap edge menggunakan dictionary
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# fungsi dijkstra untuk mencari jarak terpendek dari node awal
def dijkstra(graph, start):
    # semua jarak awal ke setiap node diset sebagai tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0
    
    # priority queue untuk menyimpan pasangan jarak dan node
    priority_queue = [(0, start)]

    while priority_queue:
        # ambil node dengan akumulasi jarak sementara paling kecil
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # jika jarak yang baru diambil lebih besar dari jarak yang tersimpan, skip proses
        if current_distance > distances[current_node]:
            continue
            
        # memeriksa se kota tetangga dari kota saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # kalau ada jarak yang lebih kecil, update jarak dan masukkan ke priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# set node awal untuk mencari jarak terpendek
node_awal = 'Bogor'

# jalankan fungsi dijkstra dan simpan hasil jarak terpendek
hasil_jarak = dijkstra(graph, node_awal)

# print hasil
print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil_jarak.items():
    print(f"{node_awal} -> {kota} = {jarak}")

# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
# Jawab: Node awal yang digunakan adalah Bogor.

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Jawab: Node yang memiliki jarak paling kecil dari node awal adalah Depok.

# 3. Node mana yang memiliki jarak paling besar dari node awal?
# Jawab: Node yang memiliki jarak paling besar dari node awal adalah Bandung.

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Jawab: Pada kasus ini, algoritma Dijkstra bekerja dengan memulai dari node awal (Bogor) dan secara iteratif memperbarui jarak ke node tetangga berdasarkan bobot edge. Algoritma menggunakan priority queue untuk memastikan bahwa node dengan jarak terpendek diproses terlebih dahulu, sehingga memastikan bahwa setiap node diproses hanya sekali dengan jarak terpendek yang benar.