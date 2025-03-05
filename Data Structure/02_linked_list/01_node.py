class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def plus(self):
        self.n += 1

    def __len__(self):
        return self.n

    ## INSERTION
    def insertHead(self, value):
        new_node = Node(value)
        self.plus()
        new_node.next = self.head
        self.head = new_node

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:  # Handle empty list
            self.head = new_node
            self.plus()
            return
        
        current = self.head
        after = int(self.n / 2)
        for i in range(after):
            current = current.next if current else None
        new_node.next = current.next if current else None
        if current:
            current.next = new_node
        self.plus()

    def insertAfter(self, after, value):
        new_node = Node(value)
        current = self.head
        while current is not None:
            if current.data == after:
                break
            current = current.next
        if current is not None:
            new_node.next = current.next
            current.next = new_node
            self.plus()
        else:
            print("ValueError: Value does not found")

    def append(self, value):
        new_node = Node(value)
        if self.head is None:  # Handle empty list
            self.head = new_node
            self.plus()
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.plus()

    ## TRAVERSE
    def __str__(self):
        if self.head is None:
            return "------------\nEmpty List\n------------"
        
        list_str = ""
        current = self.head
        while current is not None:
            list_str += str(current.data) + "-->"
            current = current.next
        return list_str[:-3]

    ## DELETION
    def clear(self):
        self.head = None
        self.n = 0

    def delFromHead(self):
        if self.head is None:
            print("List is Empty!!!")
            return
        self.head = self.head.next
        self.n -= 1 

    def pop(self):
        if self.head is None:
            print("Empty list !!!")
            return
        if self.head.next is None:  # Only one element
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
        self.n -= 1 

    def delByValue(self, value):
        
# Example usage 
list = LinkedList()
list.insertHead(5)
list.insertHead(4)
list.insertHead(3)
list.insertHead(2)
list.insertHead(1)
list.append(6)
list.append(7)
list.append(8)
list.append(9)
list.append(10)
list.append(13)


print(list)
print(len(list))

for __ in range(len(list) +3):
    list.pop()

print(list)
print(len(list))
