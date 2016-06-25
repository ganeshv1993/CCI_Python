#Reversing a string in multiple ways

#Getting input
string=raw_input().strip()
l=len(string)

#with an additional string
string1=""
for i in xrange(l-1, -1, -1):
    string1+=string[i]
print string1

#without an additional string
s=string  #just making a copy to operate on
slist=list(s)
for i in xrange(0, l/2):
    slist[i], slist[l-1-i] = slist[l-1-i], slist[i]
s=''.join(slist)
print s

#The efficient python reversal
print string[::-1]
