# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head and not head.next:
            return False
            
        slow = head
        fast = head


        while fast:
            if slow and slow.next:
                slow = slow.next
            else:
                slow = None

            if fast and fast.next and fast.next.next:
                fast = fast.next.next
            else:
                fast = None

            if slow == fast: # We've found a cycle
                return True 
        
        return False
