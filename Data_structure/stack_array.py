class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise  Exception("array is empty")
        
    def peek(self):
        if not (self.is_empty()):
            return self.items[-1]
        else:
            raise Exception("array is empty")

if __name__=="__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    print(s.peek())
    print(s.is_empty())
    print(s.items)
        
