from typing import Optional

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def mergeTwoLists(self,list1:Optional[ListNode],list2:Optional[ListNode]):
        result_list:Optional[ListNode] = ListNode(0)
        current = result_list

        while list1 and list2:
            if list1.val< list2.val:
                current.next = list1
                current = list1
                list1 = list1.next

            else:
                current.next = list2
                current = list2
                list2 = list2.next
        
        current.next = list1 if list1 else list2
        return result_list.next

    def printList(self, node: Optional[ListNode]):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)
    solution.printList(merged_list)