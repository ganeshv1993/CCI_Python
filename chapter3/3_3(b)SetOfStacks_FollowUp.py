from SetOfStacks_3_3 import SetOfStacks

def popAt(sos, stackno):
    if sos.stacksizes[stackno-1]!=0:
        if sos.stacksizes[stackno-1]!=1:
            sos.setofstacks[stackno-1].pop()
            sos.stacksizes[stackno-1]-=1
        else:
            del sos.setofstacks[stackno-1]
            del sos.stacksizes[stackno-1]
    else:
        print"Underflow Error"

sos=SetOfStacks(max_size=3)
sos.push(1)
sos.push(2)
sos.push(3)
sos.push(4)
sos.push(5)
print sos.setofstacks
popAt(sos, 2)
popAt(sos, 1)
popAt(sos, 2)
print sos.setofstacks