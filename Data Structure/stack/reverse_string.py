# Reverse the given string using stack

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
            return False
        return self.top
    def pop(self):
        if not self.isEmpty():
            self.top = self.top.next
            self.n -=1
        else:
            return False
    def __str__(self):
        stack = ''
        current = self.top
        while current != None:
            print(current.data)
            stack = stack + f'| {str(current.data)} |\n'
            current = current.next
        return stack
reverse = Stack()
string = "Hello"
for i in string:
    reverse.push(i)
print(reverse)