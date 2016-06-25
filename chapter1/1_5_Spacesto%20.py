#Replace ' ' with %20

string=raw_input().strip()
l=len(string)
i=0
while i<l:
    if string[i]==' ':
        string=string[0:i]+'%20'+string[i+1:]
        l+=2
    i+=1
print string