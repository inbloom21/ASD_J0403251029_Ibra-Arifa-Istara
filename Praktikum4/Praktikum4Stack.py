#============================================================================
# Nama        : Ibra Arifa Istara
# NIM         : J0403251029
# Kelas       : A1
#============================================================================

#============================================================================
# Implementasi Dasar: Stack
#============================================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node diinisiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke node berikutnya (awal=None)
        
#stack ada operasi push(memasukkan head baru) dan pop(menghapus head)

class Stack:
    def __init__(self):
        self.top = None #top menunjuk ke Node paling atas (awalnya kosong)
        
    def is_empty(self):
        return self.top is None # stack barang jika top = None
        
    def push(self, data): #memasukkan data baru pada stack
        #1. membuat node baru
        nodeBaru = Node(data) #instantiasi konstruktor pada class Node
        
        #2. node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top
        
        #3. geser top pindah ke node baru
        self.top = nodeBaru
    
    def pop(self): #mengambil/menghapus node paling atas(top/head)
        
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel (peek)
        self.top = self.top.next
        return data_terhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data    
    
    def tampilkan(self):
        current = self.top
        print("Top", end=" -> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
#Instantiasi Class Stack
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())
s.pop()
print("Peek (Lihat Top): ", s.peek())
