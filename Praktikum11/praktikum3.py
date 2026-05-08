# Nama: Ibra Arifa Istara
# NIM: J0403251029
# Kelas: TPL A1


def createGraph(V, edges):
    mat = [[0 for i in range(V)] for j in range(V)]

    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1
        mat[v][u] = 1
    return mat

def changeList(matrix):
    list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                list.append([i, j])
    return list

if __name__ == "__main__":
    vertex = 4
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
    graph = createGraph(vertex, edges)
    print("Adjacency Matrix:")
    for i in range(vertex):
        print(graph[i])

    print("\nAdjacency List:")
    list = changeList(graph)
    for i in range(vertex):
        print(f"{i}: ", end="")
        for j in list:
            if j[0] == i:
                print(f"{j[1]} ", end="")
        print()