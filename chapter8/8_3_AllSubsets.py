allsubsets=[]
def subsets(array):
    global allsubsets
    if len(array)==0:
        return
    if tuple(array) not in allsubsets:
        allsubsets.append(tuple(array))
    for i in range(len(array)):
        temp=array[i]
        del array[i]
        subsets(array)
        array.insert(i, temp)

array=[1,2,3,4]
subsets(array)
print allsubsets