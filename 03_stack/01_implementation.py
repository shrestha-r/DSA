import ctypes

class MeraList:
    def __init__(self):
        self.n = 0
        self.size = 1
        self.A = self.__makeArray(self.size)
    def append(self,data):
        if self.n  == self.size:
            self.__resize(self.size*2)
        self.A[self.n] = data
    def insert(self,position,data):
        if self.isEmpty():
            self.__resize(self.size*2)
        for i in range(self.n,position,-1):
            self.A[i] = self.A[i-1]
        self.A[position] = data
        self.n +=1

        self.n += 1
    def __len__(self):
        return self.n
    def __str__(self):
        list = ''
        for i in range(self.n):
            list = list + ','+ str(self.A[i])
        return '['+list.removeprefix(',')+']'
    def pop(self):
        if self.isEmpty():
            print("Empty List")
        self.A[self.n] = None
        self.n -=1
    def clear(self):
        self.n = 0
        self.size = 0
    def isEmpty(self):
        if self.n == 0:
            return True
        else:
            return False
    def __resize(self,new_capacity):
        B = self.__makeArray(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
    def __makeArray(self,capacity):
        return (capacity*ctypes.py_object)()
    


list = MeraList()

list.append(5)
list.append(5)
list.append(5)
list.append(5)
print(len(list))