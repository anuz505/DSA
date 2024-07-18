class node: 
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
       
    def push(self,new_data):
         new_node = node(new_data)
         new_node.next = self.head
         self.head = new_node
         # Time complexity = O(1)
          #To insert a node at the start/beginning/front of a Linked List, we need to:
        # Make the first node of Linked List linked to the new node
        # Remove the head from the original first node of Linked List
        # Make the new node as the Head of the Linked List.

      
    def insert_after(self, new_data, previous_node):
         if self.head is None:
            self.head = new_node
            return
         new_node = node(new_data)
         new_node.next = previous_node.next
         previous_node.next = new_node
           # Check if the given node exists or not. 
        # If it do not exists, 
        # terminate the process.
        # If the given node exists,
        # Make the element to be inserted as a new node
        # Change the next pointer of given node to the new node
        # Now shift the original next pointer of given node to the next pointer of new node

    def insert_last(self, new_data):
        if self.head is node:
            self.head = new_node
            return
        
        new_node = node(new_data)
        
        #let's traverse into last node
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
        # Time complexity : O(n)
    
def main():
        LList = LinkedList()
        LList.head = node(1)
        second = node(2)
        third = node(3)
        LList.head.next = second
        second.next = third
        LList.push(5)
        LList.insert_after(6,second)
        LList.insert_last(7)
        LList.print_list()
    

if __name__ =="__main__":
    main()
    