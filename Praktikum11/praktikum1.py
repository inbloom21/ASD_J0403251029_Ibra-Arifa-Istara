# Nama: Ibra Arifa Istara
# NIM: J0403251029
# Kelas: TPL A1


def createGraph(V, edges):
    mat = [[0 for i in range(V)] for j in range(V)] # membuat matriks dengan nilai awal 0

    for it in edges: # kalau u dan v memiliki edge, maka nilai matriks pada posisi yang menghubungkan u dan v diubah menjadi 1
        u = it[0]
        v = it[1]
        mat[u][v] = 1
        mat[v][u] = 1
    return mat # mengembalikan matriks

if __name__ == "__main__":
    vertex = 4 # jumlah vertex
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]] # edge yang menghubungkan vertex
    graph = createGraph(vertex, edges)
    print("Adjacency Matrix:") # print matriks
    for i in range(vertex):
        print(graph[i])

