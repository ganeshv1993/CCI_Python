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

def movedisks(n, current, destination, buffer):
    if n==0:
        return
    else:
        movedisks(n-1, current, buffer, destination)
        destination.push(current.array[len(current.array)-1])
        current.array.pop()
        movedisks(n-1, buffer, destination, current)

s1=stack()
s2=stack()
s3=stack()
s1.push(5)
s1.push(4)
print s1.array, s2.array, s3.array
movedisks(2,s1,s3,s2)
print s1.array, s2.array, s3.array