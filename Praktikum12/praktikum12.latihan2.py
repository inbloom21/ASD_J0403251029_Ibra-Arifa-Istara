# Nama : Ibra Arifa Istara
# NIM : J0403251029
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0
    
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Berapa jarak terpendek dari A ke B?
# Jawab: Jarak terpendek dari A ke B adalah 4.

# 2. Berapa jarak terpendek dari A ke C?
# Jawab: Jarak terpendek dari A ke C adalah 2.

# 3. Berapa jarak terpendek dari A ke D?
# Jawab: Jarak terpendek dari A ke D adalah 3.

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# Jawab: Karena total bobot dari A ke C (2) lalu D (2 + 1) adalah 3. Sedangkan bobot dari A ke B saja sudah 4 (lebih besar dari A ke D lewat C). Jadi lewat C lebih cepat.

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# Jawab: Fungsi dari priority_queue adalah untuk mengganti jarak yang paling besar dengan jarak yang lebih kecil jika ditemukan.

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
# Jawab: Karena Dijkstra tidak dapat kembali ke node yang sudah dikunjungi untuk memperbarui jarak jika ditemukan bobot negatif, sehingga bisa menghasilkan hasil yang salah.