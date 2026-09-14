# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = head

        while(n > 0):
            slow = slow.next
            n -= 1
        
        while slow:
            slow = slow.next
            fast = fast.next

        fast.next = fast.next.next
        return dummy.next