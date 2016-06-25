from LinkedList import LinkedList

def NthToLast(l,n):  #just assuming n < len of linked list
    p1=l.head
    p2=l.head
    for i in range(n):
        p1=p1.get_next()
    while p1.get_next()!=None:
        p1=p1.get_next()
        p2=p2.get_next()

    return p2.get_data()

l= LinkedList()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.insert(6)
l.insert(7)
print NthToLast(l,4)