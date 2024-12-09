import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__createArray(self.size)
    def __createArray(self,capacity):
        return (capacity*ctypes.py_object)()
    def __len__(self):
        return self.n
    def __resize(self,new_capacity):
        B = self.__createArray(new_capacity)
        self.size = new_capacity
        for i in range(0,self.n):
            B[i] = self.A[i]
        self.A = B
    def append(self,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        self.A[self.n] = item
        self.n = self.n + 1
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i])+','
        return '['+result[:-1]+']'
    def __getitem__(self,index):
        if index > self.n or index<0:
            return "indexError - Index out of range"
        else:
            return self.A[index]
    def pop(self):
        if self.n <= 0:
            return "valueError: Empty list"
        else:
            # print(self.A[self.n-1],"is removed from list.")
            self.n = self.n - 1;
    def clear(self):
        while self.n != 0:
            self.pop()
        print("list is empty now, []")
            
    def count(self,item):
        count = 0
        for i in range(self.n):
            if item == self.A[i]:
                count= count+1
        return count
    def index(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
                break;
    def insert(self,index,item):
        B = self.__createArray(self.n+8)
        for i in range(self.n):
            if i == index:
                B[i] = item
                B[i+1] = self.A[i]
            else:
                B[i+1] = self.A[i]
        return B
    def replace(self):
        pass
    def remove(self):
        ...
    def sort(self):
        ...
    def reverse(self):
        ...
            
L = [3,2,5,4]
print(L)
L.insert(1,5)
print(L)
l = MeraList()
# l.append(65)
# l.append(20)
# l.append(53)
# l.append(33)
# L = (3,3,3,3,3)
# print(L.count(3))
# print(L)
# print(L.index(3))
# l.append(10)
# # l.append(23)
# print(l[-1])
# print(l)
# for i in range(len(l)+1):
#     l.pop()
# print(l)

# l.pop()
l.append(3)
l.append(5)
l.append(3)
l.append(8)
l.append(2)
l.append(2)
l.append(4)
l.append(1)
l.append(2)
l.append(6)


print(l)
# print(l.count(3))
# print(l.index(33))
l.insert(1,2)
print(l)
# l.clear()
