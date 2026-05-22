# Nama : Ibra Arifa Istara
# NIM : J0403251029
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# Jawab: Lokasi yang paling dekat dari Gerbang adalah Kantin

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# Jawab: Waktu tempuh terpendeknya adalah 7 menit.

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# Jawab: Tidak, karena jalur langsung mungkin memiliki bobot yang lebih besar daripada jalur tidak langsung.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
# Jawab: Karena Dijkstra lebih efisien dalam menemukan jarak terpendek pada graph dengan bobot positif semua.