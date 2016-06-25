class ThreeStacks:
    def __init__(self, stack_size=10):
        self.stack_size=stack_size
        self.array=[None]*self.stack_size*3
        self.tops=[0]*3
        self.size=[0]*3

    def push(self,(stackno),data):
        if self.size[(stackno-1)]>self.stack_size:
            print "Overflow error"
        else:
            self.array[((stackno-1)*self.stack_size)+self.tops[(stackno-1)]]=data
            self.tops[(stackno-1)]+=1
            self.size[(stackno-1)]+=1

    def pop(self,(stackno)):
        if self.size[(stackno-1)]==0:
            print "Underflow error"
        else:
            self.array[((stackno-1)*self.stack_size)+self.tops[(stackno-1)]-1]=None
            self.tops[(stackno-1)]-=1
            self.size[(stackno-1)]-=1

    def peep(self,(stackno)):
        return self.array[((stackno-1)*self.stack_size)+self.tops[(stackno-1)]-1]

s=ThreeStacks(5)
s.push(1,1)
print s.array
s.push(2,1)
print s.array
s.push(3,1)
print s.array
s.push(3,2)
print s.array
s.push(2,3)
print s.array
s.pop(2)
print s.array
s.push(2,3)
print s.array
s.pop(3)
print s.array
s.pop(3)
print s.array
print s.peep(1)
print s.peep(2)
print s.peep(3)
