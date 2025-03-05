import ctypes

class MeroArray:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__makeArray(self.size)
    def __makeArray(self,capacity):
        return (capacity*ctypes.py_object)()
    def __len__(self):
        return self.n
    def __resize(self,new_size):
        B = self.__makeArray(new_size)
        self.size = new_size
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
    def append(self,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        self.A[self.n] = item
        self.n = self.n + 1
    def __str__(self):
        list = ''
        for i in range(self.n):
            list = list + str(self.A[i]) + ','
        return '['+list[:-1]+']'
    def pop(self):
        if self.n <= 0:
            print("Empty list!")
        else:
            self.size = self.n - 1    
    def clear(self):
        self.n = 0
        self.size = 0
    def index(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
                break
        return "valueError: value not found"
            
    def insert(self,pos,item):
        if self.size == self.n:
            self.__resize()
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n = self.n + 1
    def delete(self,pos):
        for i in range(pos,self.n-1):
            self.A[i] = self.A[i+1] 

        self.n = self.n - 1
list = MeroArray()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
print(len(list))
print(list)
# list.insert(3,4)
# print("inserting", list)
# print(list.index(4))
# list.pop()
# print(list)
# list.clear()
# print(list)

print(len(list))
list.insert(2,0)
print("After insertion the array look like this >>")
print(len(list))
print(list)
list.delete(2)
print(list)
print(len(list))