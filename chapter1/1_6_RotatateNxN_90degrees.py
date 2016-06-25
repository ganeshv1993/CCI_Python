#rotate nxn by 90 degrees
#let us assume the input is given as
#n
#123..n
#232..n
#.
#.
#n... n
#each row as a string

n = int(raw_input().strip())
mat=[]
for i in range(n):
    row=raw_input().strip()
    mat.append(row)

#input done. now the rotation
res=[]
for i in xrange(n):
    temp=''
    for j in xrange(n-1,-1,-1):
        temp+=mat[j][i]
    res.append(temp)

for i in xrange(n):
    print res[i]