#from platform import node
#from tkinter.messagebox import NO


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data=None):
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
        # position starts at 0
        temp1 = self.head
        if n == 0:
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

class DoublyNode():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList():
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        if data != None:
            self.insert(data)
    
    def insert(self, data):
        # insert at the head of the linked list
        temp = self.head
        n = DoublyNode(data)
        n.next = temp
        if temp:
            temp.prev = n
        self.head = n
        
        curr = n
        while curr:
            prev = curr
            curr = curr.next
        self.tail = prev


    def insertAtTail(self, data):
        # case no element exist
        # case only 1 element exists
        # case only 2 element exist
        n = DoublyNode(data)
        curr = self.tail
        if curr == None:
            self.head = n
            self.tail = n
            return n
        # need to walk through nodes
        # to find out if only an node exists
        
        # need to also worry about head

        """
        temp = curr.prev
        if temp == None:
            # only an element exists
            curr.next = n
            n.prev = curr
            self.tail = n
            # don't need to worry about updating the head
            return
        """
        # at least two nodes exist
        # curr is N1
        # new N 
        # N2<-N1<-tail
        # N2<-N1<-n<-tail
        curr.next = n
        n.prev = curr
        self.tail = n

        # N1->N2->N3->null
        # N1<-N2<-N3<-tail
        # if inserting element at tail end,
        # move element N3 and put the new element,
        # at prev N3 location.


    def delete(self, n):
        # position starts at 0
        curr = self.head

        if curr == None:
            return -1

        next = curr.next
        if n == 0:
            next.prev = None
            self.head = next
            if next.next == None:
                self.tail = next
            return 

        cnt = 1
        while next:
            if n == cnt:
                curr.next = next.next
                if next.next:
                    next.next.prev = curr
                if next.next == None:
                    self.tail = curr
                break

            curr = next
            next = next.next
            cnt += 1

    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()
    
    def printReverse(self):
        curr = self.tail
        while curr:
            print(curr.data, end=" ")
            curr = curr.prev
        print()
        

list = LinkedList()
list.reverse()
list.printList()
list.insert(1)
list.reverse()
list.insert(2)
list.insert(3)
list.reverse()
list.printList()
list.reverse()
list.printList()

dlist = DoublyLinkedList(1)
dlist.insert(2)
dlist.insert(3)
dlist.insert(4)
dlist.insert(5)
dlist.print()
dlist.delete(3)
dlist.print()
dlist.printReverse()


dlist2 = DoublyLinkedList(1)
dlist2.insertAtTail(2)
dlist2.insertAtTail(3)
dlist2.insertAtTail(4)
dlist2.insertAtTail(5)
dlist2.insertAtTail(6)
dlist2.print()
dlist2.printReverse()

dlist3 = DoublyLinkedList(1)
dlist3.insertAtTail(2)
dlist3.print()
dlist3.printReverse()

dlist4 = DoublyLinkedList(1)
dlist4.print()
dlist4.printReverse()

dlist5 = DoublyLinkedList()
dlist5.print()
dlist5.printReverse()
""""

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



"""