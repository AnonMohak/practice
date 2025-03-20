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

    def prepend(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True

    def print_ll(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next

    def get(self, index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp

    def insert(self, value, index):
        #case0-out of bounds
        if index<0 or index>=self.length:
            return False
        #case1-index=0
        if index==0:
            return self.prepend(value)
        #case2-index=self.len
        if index==self.length:
            return self.append(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True


my_ll = LinkedList(0)
my_ll.append(1)
my_ll.append(2)
my_ll.append(3)
my_ll.insert(10, 1)
my_ll.print_ll()
