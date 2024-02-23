#Data Structure: Stack
#Stack implementation using a linked list
#
#isEmpty() --> Returns whether the stack is empty --> O(1)
#getSize() --> Returns size of stack --> O(1)
#top() / peek() --> Returns reference to topmost element of stack --> O(1)
#push(a) --> Inserts element 'a' at the top of the stack --> O(1) 
#pop() --> Deletes the topmost element of the stack --> O(1)
#

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    #Stack initialization, using dummy node
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    
    #String representation of stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]
    
    #Gets current size of stack
    def getSize(self):
        return self.size
    
    #Checks if stack is empty returns boolean
    def isEmpty(self):
        return self.size == 0
    
    #Get top item from stack
    def peek(self):
        if self.isEmpty():
            raise Exception("This is an empty stack")
        return self.head.next.value
    
    #Put value into stack
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    
    #Remove value from stack and return
    def pop(self):
        if self.isEmpty():
            raise Exception("This is an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")