class Node:
    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node=next_node
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self, node):
        self.next_node=node

class LinkedList:
    def __init__(self):
        self.head=None

    def get_length(self):
        itr=self.head
        count=0
        while itr!=None:
            count+=1
            itr=itr.get_next()
        return(count)

    def insert(self,data):
        temp_node=Node(data)
        temp_node.set_next(self.head)
        self.head=temp_node

    def delete_node(self,data):
        node=self.head
        prev_node=self.head
        flag=False
        while node!=None:
            if node.get_data()==data:
                if node==self.head:
                    self.head=node.get_next()
                else:
                    prev_node.set_next(node.get_next())
                flag=True
                break
            prev_node=node
            node=node.get_next()

        if flag==False:
            print "Not found"
        else:
            "Deleted"

    def printlist(self):
        node=self.head
        while node!=None:
            print node.get_data()
            node=node.get_next()