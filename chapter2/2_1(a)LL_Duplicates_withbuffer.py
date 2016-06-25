from LinkedList import LinkedList

def RemoveDuplicates_withbuffer(l):
    table=[]
    node=l.head
    while node!=None:
        if node.get_data() in table:
            prev_node.set_next(node.get_next())
            node=node.get_next()
        else:
            table.append(node.get_data())
            prev_node=node
            node=node.get_next()

l= LinkedList()
l.insert(2)
l.insert(2)
l.insert(4)
l.insert(5)
l.insert(6)
l.insert(5)
l.insert(2)
RemoveDuplicates_withbuffer(l)
l.printlist()