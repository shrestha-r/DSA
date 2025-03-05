class Node:
    def __init__(self,data):
        self.data = data
        self.after = None
class Queue():
    def __init__(self):
        self.n = 0
        self.front = None
    def enqueue(self,data):
        new_node = Node(data)
        self