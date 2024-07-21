class Queue:
    def __init__(self,capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.q = [None] * capacity
        self.capacity = capacity
    
    def isEmpty(self):
        return (self.size == 0)
    
    def isFull(self):
        return (self.size == self.capacity)
    
    def enqueue(self, item):
        if self.isFull():
            print("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = item
        self.size = self.size + 1
        print(f"{self.rear} is enqueued")
        
    def dequeu(self):
        if self.isEmpty():
            print("queue is empty")
        print("% s dequeued from queue" % str(self.q[self.front]))
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1 
    
    def front(self):
        print(self.q[self.front])
    
    def rear(self):
        print(self.q[self.rear])

    def printAll(self):
        for i in range(self.size):
            print(self.q[(self.front + i) % self.capacity])

        

# Driver Code
if __name__ == '__main__':
 
    queue = Queue(30)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.dequeu()
    queue.front
    queue.rear
    print('\n')
    queue.printAll()
