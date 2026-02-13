class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Tambahkan pointer tail

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node # Tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node # Sambungkan tail ke node baru
            self.tail = new_node # Update tail ke node baru

    def simpan(self):
        temp = self.head
        list1 = []
        while temp:
            list1.append(temp)
            temp = temp.next

def reverse(self):
    temp = self.head
    reverse_list = []
    while temp:
        reverse_list.insert(0, temp)
        temp = temp.next

dll = LinkedList()

masukan = input("Masukkan elemen untuk Linked List: ").split(", ")
for i in masukan:
    dll.insert_at_end(int(i))

listluar = dll.simpan()