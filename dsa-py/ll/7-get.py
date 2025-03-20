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

    def get(self, index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
        #return temp.value


my_ll = LinkedList(0)
my_ll.append(1)
my_ll.append(2)
my_ll.print_ll()
print(my_ll.get(1))

