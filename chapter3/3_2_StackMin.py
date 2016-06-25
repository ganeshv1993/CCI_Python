class stack:

    def __init__(self):
        self.array=list()
        self.minarray=list()

    def push(self,data):
        self.array.append(data)
        if len(self.minarray)>0:
            self.minarray.append(min(data, self.minarray[len(self.minarray)-1]))
        else:
            self.minarray.append(data)

    def pop(self):
        self.array.pop()
        self.minarray.pop()

    def min(self):
        return self.minarray[len(self.minarray)-1]

s=stack()
s.push(5)
s.push(2)
s.push(3)
s.push(3)
s.push(-1)
s.pop()
print s.min()

