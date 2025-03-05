class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.n = 0
        self.top = None
    def __len__(self):
        return self.n
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.n+=1
    def isEmpty(self):
        return self.n == 0

    def pop(self):
        if not self.isEmpty():
            current = self.top
            self.top = self.top.next
            self.n -=1
            return current.data
        else:
            return "Empty List"
    def peek(self):
        if self.isEmpty():
            return "Empty List"
        else:
            peek = self.top
            return peek.data
    def __str__(self):
        stack = ''
        current = self.top
        while current != None:
            stack = stack + f'| {str(current.data)} |\n'
            current = current.next
        return stack

def undo_redu(string, cmd):
    undo = Stack()
    for j in string:
        undo.push(j)
    redo = Stack()
    for i in cmd:
        if i == 'u':
            redo.push(undo.pop())
        if i ==  'r':
            if redo.isEmpty():
                continue
            undo.push(redo.peek())
    return undo

text = undo_redu("stringisgood","uururuu")
print(text)