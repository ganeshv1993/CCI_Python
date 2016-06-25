from LinkedList import LinkedList

def RemoveDuplicates_withoutbuffer(l):
    node=l.head
    while node!=None:
        temp=node.get_next()
        prev_node=node
        while temp!=None:
            if temp.get_data() == node.get_data():
                prev_node.set_next(temp.get_next())
                temp=temp.get_next()
            else:
                prev_node=temp
                temp=temp.get_next()
        node=node.get_next()

l= LinkedList()
l.insert(2)
l.insert(2)
l.insert(4)
l.insert(5)
l.insert(6)
l.insert(5)
l.insert(2)
RemoveDuplicates_withoutbuffer(l)
l.printlist()