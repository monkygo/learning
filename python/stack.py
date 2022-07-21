from linkedlist import LinkedList

class Stack():
    def __init__(self):
        self.list = LinkedList()

    def push(self, x):
        self.list.insert(x)

    def pop(self):
        n = self.list.head
        if n == None:
            return
        self.list.delete(0)
        return n
    
    def top(self):
        return self.list.head

    def isEmpty(self):
        return self.list.head == None

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

        
