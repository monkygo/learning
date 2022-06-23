#from platform import node
#from tkinter.messagebox import NO


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
            n = Node(data)
            n.next = self.head
            self.head = n
            return n
    
    def insertAt(self, data, i):
        n = Node(data)

        if i == 0:
            n.next = self.head
            self.head = n

        curr = self.head
        cnt = 0
        while curr:
            cnt += 1
            prev = curr
            curr = curr.next
            if cnt == i:
                n.next = curr
                prev.next = n
                break
            
    
    def insertAfter(self, node, data):
        if node:
            n = Node(data)
            n.next = node.next
            node.next = n
    
    def delete(self, n):
        temp1 = self.head
        if n == 1:
            self.head = temp1.next
            temp1 = None
            return
        
        cnt = 0
        while cnt < n - 2:
            cnt += 1
            temp1 = temp1.next

        temp2 = temp1.next
        temp1.next = temp2.next
        temp2 = None

    def append(self, data):
        temp = self.head
        last = temp
        while temp:
            last = temp
            temp = temp.next
        
        n = Node(data)
        if last:
            last.next = n
        else:
            self.head = n

    def reverse(self):

        # at the first node
        # set  first node next to null
        temp1 = self.head
        temp2 = temp1.next
        temp1.next = None
        while temp2:
            next = temp2.next
            temp2.next = temp1
            temp1 = temp2
            temp2 = next
        self.head = temp1

    def reverse2(self):
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
            
    def length(self):
        cnt = 0
        temp = self.head
        while temp:
            cnt += 1
            temp = temp.next
        return cnt

    def print(self):
        # loop through list
        n =  self.head
        print(n.data, end=" ")
        while n.next != None:
            #print(n.data)
            n = n.next
            print(n.data, end=" ")
        #print(n.data)
        print("")
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("")


list = LinkedList(0)
list.insert(2)
list.insert(3)
n4 = list.insert(4)
list.insert(11)
list.insertAfter(n4, 5)
list.append(99)
list.printList()

#list.print()
#list.printList()

list2 = LinkedList()
list2.append(1)
list2.append(2)
list2.append(7)
list2.printList()
print("length:", list2.length())

list3 = LinkedList()
list3.insertAt(0, 0)
list3.insertAt(10, 0)
list3.insertAt(1, 1)
list3.insertAt(2, 2)
list3.insertAt(4, 2)
list3.insertAt(3, 3)
list3.insertAt(5, 5)
list3.insertAt(7, 7)
#list3.insertAt(5, 3)
#print("missing head:", list3.head)
list3.printList()
list3.delete(3)
list3.delete(3)
list3.printList()
list3.reverse2()
list3.printList()

