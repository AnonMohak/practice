class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True

    def print_ll(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
            self.length=0
            #return temp
            return temp.value
        self.head=self.head.next
        temp.next=None
        self.length-=1
        #return temp
        return temp.value  


my_ll = LinkedList(0)
my_ll.append(1)
my_ll.append(2)
my_ll.pop_first()
my_ll.print_ll()
