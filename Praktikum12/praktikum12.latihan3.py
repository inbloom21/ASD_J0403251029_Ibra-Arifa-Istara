# Nama : Ibra Arifa Istara
# NIM : J0403251029
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================
# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}
def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B?
# Jawab: Bobot langsung dari A ke B adalah 5.

# 2. Berapa total bobot jalur A -> C -> B?
# Jawab: Total bobot jalur A -> C -> B adalah 2 (Karena 4 + (-2)).

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# Jawab: Jalur A -> C -> B. Karena jaraknya adalah 2, lebih kecil dibandingkan dengan jalur langsung A -> B yang memiliki bobot 5.

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# Jawab: Karena Bellman-Ford memeriksa semua edge secara berulang dan dapat menangani penurunan jarak yang terjadi akibat bobot negatif, sehingga dapat menemukan jarak terpendek meskipun ada edge dengan bobot negatif.

# 5. Apa yang dimaksud dengan proses relaksasi edge?
# Jawab: Proses relaksasi edge adalah proses di mana algoritma memeriksa apakah jarak ke suatu node melalui edge tertentu lebih kecil dibandingk jarak yang sudah diketahui sebelumnya. Jika ya, maka jarak tersebut diperbarui dengan nilai yang lebih kecil.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
# Jawab: Bellman-Ford dapat menangani graph dengan bobot negatif, sedangkan Dijkstra tidak dapat menangani bobot negatif.