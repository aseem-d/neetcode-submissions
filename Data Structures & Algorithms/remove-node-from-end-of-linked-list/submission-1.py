# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        node = head
        while node:
            node = node.next
            N += 1
        k = N - n
        node = head
        if k == 0:
            return head.next
        while k > 1:
            node = node.next
            k -= 1
        
        if node.next.next:
            node.next = node.next.next
        else:
            node.next = None
        
        return head
        