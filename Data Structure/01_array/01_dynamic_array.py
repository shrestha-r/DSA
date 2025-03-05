import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0

        # ctype array with size = self.size
        self.A = self.__make_array(self.size)

        # creates c type array(static, referentail) with size capacity
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    def __len__(self):
        return self.n
    def __resize(self,new_size):
        # create a new arrary with new capacity
        B = self.__make_array(new_size)
        self.size = new_size

        # copy the content of A to B
        for i in range(self.n): 
            B[i] = self.A[i]
        # reassign
        self.A = B

        
    def append(self,item):
        if self.size == self.n:
            self.__resize(self.size*2)
        self.A[self.n] = item
        self.n = self.n + 1 
    def __str__(self):
        list = ''
        for i in range(0,self.n):
            list = list + str(self.A[i]) + ","
        
        return "("+ str(list).removesuffix(',') + ")"

L = MeraList()
# print(type(L))
# print(L)

print(len(L))

L.append(4.5)
L.append(4)
L.append("hello")
L.append(True)

print("The size of Array is ", len(L))
print(L)