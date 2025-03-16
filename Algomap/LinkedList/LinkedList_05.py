from typing import Optional

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def middlenode(self,head:Optional[ListNode]):
        if not head or not head.next:
            return head
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def printList(self, node: Optional[ListNode]):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")
    
    def printnode(self, node:Optional[ListNode]):
        if node:
            print (node.val)


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    solution = Solution()
    middlenode = solution.middlenode(list1)
    solution.printList(list1)
    solution.printnode(middlenode)