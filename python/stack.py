from linkedlist import DoublyLinkedList

class Stack():
    def __init__(self):
        self.list = DoublyLinkedList()

    def push(self, x):
        self.list.insertAtTail(x)

    def pop(self):
        curr = self.list.head

        if curr == None:
            return

        cnt = -1
        while curr:
            curr = curr.next
            cnt += 1

        n = self.list.tail
        self.list.delete(cnt)
        return n
    
    def top(self):
        return self.list.tail

    def isEmpty(self):
        return self.list.tail == None

    def print(self):
        self.list.print()

s = Stack()
print("isEmpty: ", s.isEmpty())
s.push(1)
s.push(2)
s.push(3)
s.print()
print("isEmpty: ", s.isEmpty())
print("pop: ", s.pop().data)
print("top: ", s.top().data)

        
