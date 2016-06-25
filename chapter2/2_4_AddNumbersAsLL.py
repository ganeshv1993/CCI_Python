from LinkedList import LinkedList

def add(l1,l2):
    n1=l1.head
    n2=l2.head
    result=LinkedList()
    carry=0
    if l1.get_length()>= l2.get_length():
        bigger=n1
        smaller=n2
    else:
        bigger=n2
        smaller=n1
    while bigger!=None:
        if smaller==None:
            s=bigger.get_data()+carry
            result.insert(s%10)
            carry=s/10
        else:
            s=bigger.get_data()+smaller.get_data()+carry
            result.insert(s%10)
            carry=s/10
            smaller=smaller.get_next()
        bigger=bigger.get_next()
    if carry!=0:
        result.insert(carry)
    return result


l1=LinkedList()
l2=LinkedList()

l1.insert(5)
l1.insert(1)
l1.insert(3)

l2.insert(6)
l2.insert(9)
l2.insert(5)
l2.insert(1)

result=add(l1,l2)
result.printlist()