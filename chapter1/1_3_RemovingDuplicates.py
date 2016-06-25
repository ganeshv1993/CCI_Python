#Removing duplicates with no additional memory

string=raw_input().strip()
l=len(string)
i=0
while i<l:
    if string[i] in string[0:i]:
        string= string[0:i]+string[i+1:]
        l-=1
        i-=1
    i+=1
print string