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
        if self.head==None:
            self.head=new_node
            self.tail=mew_node
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

    def prepend(self, value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True


my_ll = LinkedList(0)
my_ll.append(1)
my_ll.append(2)
my_ll.prepend(-1)
my_ll.print_ll()
