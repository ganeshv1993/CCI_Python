class SetOfStacks:
    def __init__(self, max_size=10):
        self.max_size=max_size
        self.setofstacks=[]
        self.stacksizes=[]

    def push(self, data):
        if (len(self.setofstacks)==0) or (self.stacksizes[len(self.stacksizes)-1]==self.max_size):
            temp=[data]
            self.setofstacks.append(temp)
            self.stacksizes.append(1)
        else:
            self.setofstacks[len(self.setofstacks)-1].append(data)
            self.stacksizes[len(self.stacksizes)-1]+=1

    def pop(self):
        if len(self.setofstacks)==0:
            print"Underflow error"
        elif self.stacksizes[len(self.stacksizes)-1]==1:
            self.stacksizes.pop()  #using the inbuilt pop() function of list datatype
            self.setofstacks.pop()
        else:
            self.setofstacks[len(self.setofstacks)-1].pop()
            self.stacksizes[len(self.stacksizes)-1]-=1

sos=SetOfStacks(max_size=3)
sos.push(1)
sos.push(2)
sos.push(3)
sos.push(4)
sos.push(5)
print sos.setofstacks
sos.pop()
sos.pop()
sos.pop()
sos.pop()
print sos.setofstacks