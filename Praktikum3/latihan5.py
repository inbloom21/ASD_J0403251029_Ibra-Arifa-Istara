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

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

dll = LinkedList()

masukan = input("Masukkan elemen untuk Linked List: ").split(", ")
for i in masukan:
    dll.insert_at_end(int(i))

print("Linked list sebelum dibalik: ", end="")
dll.display()

dll.reverse()
print("Linked list setelah dibalik: ", end="")
dll.display()