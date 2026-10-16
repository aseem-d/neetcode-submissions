# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2

        new_list = ListNode()
        tail = new_list
        while node1 and node2:
            if node1.val <= node2.val:
                tail.next = node1
                tail = tail.next
                node1 = node1.next
            else:
                tail.next = node2
                tail = tail.next
                node2 = node2.next
        while node1:
            tail.next = node1
            tail = tail.next
            node1 = node1.next
        while node2:
            tail.next = node2
            tail = tail.next
            node2 = node2.next 
        
        return new_list.next

        
        