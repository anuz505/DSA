# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return temp
    
if __name__ =="__main__":
    # Helper function to create a linked list from a list
    def create_linked_list(arr: List[int]) -> Optional[ListNode]:
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    # Helper function to print a linked list
    def print_linked_list(head: Optional[ListNode]) -> None:
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next

    # Example usage
    lst = [1, 1, 2, 3, 3]
    linked_list = create_linked_list(lst)
    solution = Solution()
    result = solution.deleteDuplicates(linked_list)
    print_linked_list(result)
        