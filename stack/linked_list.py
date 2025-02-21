class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.n = 0
        self.head = None
    def __len__(self):
        return self.n
    def HeadInsert(self,data):
        current = Node(data)
        current.next = self.head
        self.n += 1



list = LinkedList()
list.HeadInsert(5)
list.HeadInsert(5)
list.HeadInsert(5)
print(len(list))