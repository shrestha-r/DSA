class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
    def __len__(self):
        return self.n
    def insertHead(self):
      ...
        