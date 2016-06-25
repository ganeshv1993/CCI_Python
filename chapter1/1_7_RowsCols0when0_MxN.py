#rotate nxn by 90 degrees
#let us assume the input is given as
#m n
#123..n
#232..n
#.
#.
#m... n
#each row as a string

m,n = map(int,(raw_input().strip().split(' ')))
mat=[]
for i in xrange(m):
    row=raw_input().strip()
    mat.append(row)

rows=[]
cols=[]
for i in xrange(m):
    for j in xrange(n):
        if int(mat[i][j])==0:
            rows.append(i)
            cols.append(j)
for i in xrange(m):
    for j in xrange(n):
        if (i in rows) or (j in cols):
            temp=list(mat[i])
            temp[j]='0'
            mat[i]=''.join(temp)
for i in xrange(m):
    print mat[i]