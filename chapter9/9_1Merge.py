def merge(a,b):
    for i in range(len(b)):
        ind=0
        while ind<len(a) and b[i]>a[ind]:
            ind+=1
        a.insert(ind,b[i])


a=[1,3,4,5,7]
b=[1,2,3,4,5,6,7,8]
merge(a,b)
print a