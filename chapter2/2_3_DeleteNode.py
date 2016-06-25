from LinkedList import LinkedList

def delete(l,delnode):  #just assuming n < len of linked list
    node=l.head
    prev_node=l.head
    while node!=delnode:
        prev_node=node
        node=node.get_next()
    prev_node.set_next(node.get_next())

l= LinkedList()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
temp=l.head #we delete this node with data 4
l.insert(5)
l.insert(6)
l.insert(7)
delete(l,temp)
l.printlist()