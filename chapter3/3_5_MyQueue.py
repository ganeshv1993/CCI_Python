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

class MyQueue:
    def __init__(self):
        self.size=0
        self.s1=stack()
        self.s2=stack()

    def add(self, data):
        self.s1.push(data)

    def remove(self):
        while self.s1.empty()==False:
            self.s2.push(self.s1.peep())
            self.s1.pop()
        self.s2.pop()
        while self.s2.empty()==False:
            self.s1.push(self.s2.peep())
            self.s2.pop()

mq=MyQueue()
mq.add(1)
mq.add(2)
mq.add(3)
print mq.s1.array
mq.remove()
mq.remove()
print mq.s1.array


