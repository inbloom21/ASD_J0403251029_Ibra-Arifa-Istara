# Nama: Ibra Arifa Istara
# NIM: J0403251029
# Kelas: TPL A1


def createGraphMatrix(edges):
    nodes = []

    for u, v in edges:
        if u not in nodes:
            nodes.append(u)
        if v not in nodes:
            nodes.append(v)
    
    V = len(nodes)
    mat = [[0 for _ in range(V)] for _ in range(V)]

    for u, v in edges:
        uIndex = nodes.index(u)
        vIndex = nodes.index(v)
        
        mat[uIndex][vIndex] = 1
        mat[vIndex][uIndex] = 1
        
    return mat

def createGraphList(edges):
    adj = {}

    for it in edges:
        u = it[0]
        v = it[1]

        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []

        adj[u].append(v)
        adj[v].append(u)

    return adj

if __name__ == "__main__":
    jalan = [["New York", "Albany"], ["Albany", "Schenectady"], ["Binghamton", "Schenectady"], ["Binghamton", "New York"], ["Schenectady", "Syracuse"], ["Syracuse", "Binghamton"]]
    graphmatrix = createGraphMatrix(jalan)
    graphlist = createGraphList(jalan)

    print("\nNode: Kota")
    print("Nodes: New York, Albany, Schenectady, Binghamton, Syracuse")
    print("Hubungan Antar Node: Jalan\n")

    print("Adjacency Matrix:")
    for row in graphmatrix:
        print(row)

    print("\nAdjacency List:")
    for i in graphlist:
        print(f"{i}: {graphlist[i]}")