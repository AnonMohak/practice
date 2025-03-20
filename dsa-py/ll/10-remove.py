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
        while temp:
            print(temp.value)
            temp=temp.next

    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
            self.length=0
            return temp
        prev=self.head
        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        return temp

    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
            self.length=0
            return temp
        self.head=self.head.next
        temp.next=None
        self.length-=1
        return temp

    def get(self, index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp

    def set(self, value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False

    def remove(self, index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        prev=self.get(index-1)
        temp=prev.next
        prev.next=temp.next
        temp.next=None
        self.length-=1
        return temp


my_ll = LinkedList(0)
my_ll.append(1)
my_ll.append(2)
my_ll.append(3)
my_ll.print_ll()
print('+++++++++++++++++++++++++++++')
#my_ll.remove(2)
my_ll.remove(1)
#my_ll.remove(1)
my_ll.print_ll()









