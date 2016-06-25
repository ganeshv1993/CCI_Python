def isSubstring(s1,s2):
    if s1 in s2:
        return True
    else:
        return False

string1=raw_input().strip()
string2=raw_input().strip()


if len(string1)!=len(string2):
    print "Not a rotation"
else:
    string1=string1+string1
    if(isSubstring(string2, string1)):
        print "Yes, it is a rotation"
    else:
        print "Not a rotation"