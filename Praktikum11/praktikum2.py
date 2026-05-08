# Nama: Ibra Arifa Istara
# NIM: J0403251029
# Kelas: TPL A1

def createGraph(edges):
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
    edges = [["A", "B"], ["A", "C"], ["D", "B"], ["C", "D"]]
    graph = createGraph(edges)
    
    for i in graph:
        print(f"{i}: {graph[i]}")