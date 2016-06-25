#part b. without additional data structure

string=raw_input().strip()
l=len(string)
flag=False
for i in xrange(l):
    if string[i] in string[i+1:]:
        flag=True
        break
if flag==True:
    print "Has duplicate characters"
else:
    print "All characters are unique"