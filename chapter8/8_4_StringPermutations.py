AllPermutations=[]

def permutations(s):
    res=[]
    if len(s)==1:
        res=[s]
    else:
        for i in range(len(s)):
            s1=list(s[i])
            s2=s[0:i]+s[i+1:]
            res+=([s1+perms for perms in permutations(s2)])
    return res

s="ABC"
length=len(s)
s=list(s)
res= permutations(s)

print "Result", res
