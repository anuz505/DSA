class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        pop_value = self.head.data
        self.head = self.head.next
        return pop_value
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head.data
    
    def printall(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next
    
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.is_empty())
    print(f"removed {s.pop()}")
    print(f"peek {s.peek()}") 
    print('\n')
    s.printall()
    
        