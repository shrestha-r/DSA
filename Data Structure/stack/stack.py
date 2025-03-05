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
        return self.n == None
    def peek(self):
        if self.isEmpty():
            return "Empty List"
        return self.top
    def pop(self):
        if not self.isEmpty():
            self.top = self.top.next
            self.n -=1
        else:
            return "Empty List"
    def __str__(self):
        stack = ''
        current = self.top
        while current != None:
            stack = stack + f'| {str(current.data)} |\n'
            current = current.next
        return stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(7)
stack.push(9)
stack.push(8)
stack.push(0)
print(stack)
print("length is ",len(stack))
stack.pop()
print(stack)
print(len(stack))