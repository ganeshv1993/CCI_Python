class stack:

    def __init__(self):
        self.array=list()

    def push(self,data):
        self.array.append(data)

    def pop(self):
        self.array.pop()

    def peep(self):
        return self.array[len(self.array)-1]

    def empty(self):
        if len(self.array)==0:
            return True
        else:
            return False

def sort(s1):
    s2=stack()
    s2.push(s1.peep())
    s1.pop()
    print s2.array, s1.array
    while s1.empty()!=True:
        temp=s1.peep()
        s1.pop()
        while (s2.empty()!=True) and (s2.peep()>temp):
            s1.push(s2.peep())
            s2.pop()
        s2.push(temp)
        print s2.array
        print s1.array
    print s2.array

s1=stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(1)
sort(s1)
