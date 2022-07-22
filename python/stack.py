from linkedlist import LinkedList

# =================================================
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

# =================================================
def reverseStr(str, buildStr, start):
    if start >= len(str) - 1:
        return str[start]
    s = str[start]
    start += 1
    return reverseStr(str, buildStr, start) + s

# =================================================
# check for balanced parentheses, { [ ( ) ] }
def checkForBalancedParentheses(str):
    stack = Stack()
    openingingParantheses = {"{":"}", "[":"]", "(":")"}
    closingParantheses = {"}":"{", "]":"[", ")":"("}

    for x in str:
        if x in openingingParantheses:
            stack.push(x)
        elif x in closingParantheses:
            if stack.isEmpty() == True or closingParantheses[x] != stack.top().data:
                return False
            else:
                lastOpenParanthesis = stack.pop().data
 
    return stack.isEmpty()

# =================================================
# =================================================

s = Stack()
print("isEmpty: ", s.isEmpty())
s.push(1)
s.push(2)
s.push(3)
s.print()
print("isEmpty: ", s.isEmpty())
print("pop: ", s.pop().data)
print("top: ", s.top().data)

        
# reverse a string
stx = Stack()
s1 = "Hello"
for x in s1:
    stx.push(x)
stx.print()
arr = []

while stx.isEmpty() == False:
    arr.append(stx.pop().data)
s2 = "".join(arr)
print("s2:", s2)

j = len(s1) - 1
i = 0
sArr1 = list(s1)
while j > i:
    temp = sArr1[i]
    sArr1[i] = sArr1[j]
    sArr1[j] = temp
    i += 1
    j -= 1
print("sArr1:", sArr1)
print("sArr1 string:", "".join(sArr1))

print("revStr: ", reverseStr("Hello", "", 0))

str = "{ [ ( ) ] }"
print("check for balanced parantheses:", checkForBalancedParentheses(str))
str = "{ [ ( ) ] } )"
print("check for balanced parantheses:", checkForBalancedParentheses(str))
str = "{ [zdf ( ) ]basdf } a"
print("check for balanced parantheses:", checkForBalancedParentheses(str))
str = "{ [ ) ( ) ] } )"
print("check for balanced parantheses:", checkForBalancedParentheses(str))
