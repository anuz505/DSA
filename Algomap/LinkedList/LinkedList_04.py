from typing import Optional

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
        def hasCycle(self, head: Optional[ListNode]) -> bool:
            hashset = set()
            while head:
                
                 if head in hashset:
                      return True
                 hashset.add(head)
                 head = head.next


            return False
        
        def hasCycleFloydAlgorithm(self, head: Optional[ListNode]) -> bool :
             if not head or not head.next:
                  return False

             slow = fast = head

             while fast and fast.next:
                  fast = fast.next.next
                  slow = slow.next

                  if slow in fast:
                       return True
             return False
        
if __name__ == "__main__":
     node1 = ListNode(3)
     node2 = ListNode(2)
     node3 = ListNode(0)
     node4 = ListNode(-4)
    
     node1.next = node2
     node2.next = node3
     node3.next = node4
     node4.next = node2  # Creates a cycle
 
     solution = Solution()
     print(solution.hasCycleFloydAlgorithm(node1))  # Output: True

        