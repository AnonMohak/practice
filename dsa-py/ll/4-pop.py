class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def pop(self):
        #when the list is empty
        if self.length == 0:
            return None

        temp=self.head

        #when list has 1 element
        if self.length==1:
            self.head=None
            self.tail=None
            self.length=0
            return temp


        #when list have 2 or more elements
        pre=self.head

        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1

        return temp



my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.pop()
my_ll.print_ll()
