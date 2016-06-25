string=raw_input().strip()
ascii_list=[False]*256
if len(string)>256:
    print "Duplicate chars present"
else:
    flag= False
    for ch in string:
        if ascii_list[ord(ch)]==True:
            flag=True
            break
        else:
            ascii_list[ord(ch)]=True
    if flag==True:
        print "Duplicate Characters present"
    else:
        print "All characters are unique"