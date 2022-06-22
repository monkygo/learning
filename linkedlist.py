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
            return self.head
        else:
            temp = self.head
            n = Node(data)
            n.next = temp
            self.head = n
            return n
    
    def insertAfter(self, node, data):
        if node:
            n = Node(data)
            n.next = node.next
            node.next = n

    def print(self):
        # loop through list
        n =  self.head
        print(n.data, end=" ")
        while n.next != None:
            #print(n.data)
            n = n.next
            print(n.data)
        #print(n.data)
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


list = LinkedList(0)
list.insert(2)
list.insert(3)
n4 = list.insert(4)
list.insert(11)
list.insertAfter(n4, 5)
#list.print()
list.printList()


