#Anagrams

string1=raw_input().strip()
string2=raw_input().strip()

if len(string1)!=len(string2):
    print "They are not anagrams"
else:
    l=len(string1)
    flag=False
    for ch in string1:
        if ch in string2:
            ind=string2.index(ch)
            string2=string2[0:ind]+string2[ind+1:]
        else:
            flag=True
            break
    if flag==True:
        print "Not anagrams"
    else:
        print "Anagrams"