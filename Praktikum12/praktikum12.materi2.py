# Nama : Ibra Arifa Istara
# NIM : J0403251029
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path

def bellman_ford(graph, start):
    # set jarak awal ke semua node sebagai tak hingga
    distances = {node: float('inf') for node in graph}
    # jarak dari node awal ke diri sendiri adalah 0
    distances[start] = 0

    # Relaksasi berulang
    for _ in range(len(graph) - 1):
        
        for node in graph:

            for neighbor, weight in graph[node].items():
                
                if distances[node] + weight < distances[neighbor]:

                    distances[neighbor] = distances[node] + weight

    return distances