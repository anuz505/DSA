
from typing import Optional

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        prev_node = None
        temp = None
        while current_node:
            temp = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = temp

        return prev_node
    
    def reverseList_recursive(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head
        
 
        