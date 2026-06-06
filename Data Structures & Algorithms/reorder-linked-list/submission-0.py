# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev, l1, l2 = None, head, slow.next
        slow.next = None

        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        
        l2 = prev 
        while l2:
            t1, t2 = l1.next, l2.next
            l1.next = l2
            l2.next = t1
            l1, l2 = t1, t2
        
        
        
