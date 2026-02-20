#============================================================================
# Nama        : Ibra Arifa Istara
# NIM         : J0403251029
# Kelas       : A1
#============================================================================

#============================================================================
# Implementasi Dasar: Node Pada Linked List
#============================================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node diinisiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke node berikutnya (awal=None)
        
#1.) membuat node dengan instantiasi class Node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2.) mendefinisikan head dan menghubungkan Node: A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3.) menelusuri Node dari head sampai ke None (Traversal)
current = head
while current is not None:
    print(current.data) #menampilkan data pada Node saat ini
    current = current.next #pindah ke Node berikutnya