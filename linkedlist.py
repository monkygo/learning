from tkinter.messagebox import NO


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data = None):
        self.head = None
        if data != None:
            self.insert(data)

    def insert(self, data):
        # insert at the head
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            n = Node(data)
            n.next = temp
            self.head = n

    def print(self):
        # loop through list
        n =  self.head
        print(n.data)
        while n.next != None:
            #print(n.data)
            n = n.next
            print(n.data)
        #print(n.data)


list = LinkedList(0)
list.insert(2)
list.insert(3)
list.insert(4)
list.insert(11)
list.print()


