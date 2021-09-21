class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next


list = LinkedList()
list.head = Node("mon")
e2 = Node("tues")
e3 = Node("wed")
e4 = Node("thurs")
e5 = Node("fri")
list.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
list.listprint()


exit()
