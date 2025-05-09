class Stack():
  def __init__(self):
    self.stack = []
    self.n = 0
  def __len__(self):
    return self.n
  def append(self,item):
    self.stack.append(item)
    self.n +=1
  def pop(self,item):
    self.n -= 1
    return self.stack.pop()
  def peek(self):
    return self.stack[-1]
  def isEmpty(self):
    return len(self.stack) == 0
  def __str__(self):
    string = ''
    for i in self.stack:
       string = str(i) + '\n' +string
    return string

stack = Stack()
stack.append(4)
stack.append(1)
stack.append(3)
print(len(stack))
print(stack)