#given we have a circular linked list as specified

def findLoopbegining(l):
    n1=l.head
    n2=l.head

    while(n2.next!=None):
        n1=n1.next
        n2=n2.next.next
        if n1==n2:
            break

    if n2.next==None:
        return -1

    n1=l.head
    while n1!=n2:
        n1=n1.next
        n2=n2.next
    return n2

